from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import  HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, schemas
from app.models.user import User
from app.core.config import settings
from app.db.session import SessionLocal

'''
Define o esquema de segurança, informando que o token será obtido
no endpoint /api/v1/auth/login
'''

reusable_oauth2 = HTTPBearer()

def get_db() -> Generator:
    """
    Dependência para obter uma sessão de banco de dados.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db),
    # A dependência agora retorna um objeto, não uma string
    token: HTTPAuthorizationCredentials = Depends(reusable_oauth2),
) -> User:
    """
    Dependência para obter o usuário atual a partir de um token JWT.
    """
    try:
        token_str = token.credentials

        payload = jwt.decode(
            token_str, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = schemas.TokenData(email=payload.get("sub"))
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = crud.user.get_by_email(db, email=token_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Dependência para verificar se o usuário atual é um superusuário ativo.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403, detail="O usuário não tem privilégios suficientes"
        )
    return current_user