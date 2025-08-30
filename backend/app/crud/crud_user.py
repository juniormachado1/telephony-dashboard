from sqlalchemy.orm import Session
from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate 

class CrudUser:

    def get(self, db: Session, id: int) -> User | None:
        return db.query(User).filter(User.id == id).first()
    
    def get_by_email(self, db: Session, *, email: str) -> User | None:
        """
        Busca um usuário no banco de dados pelo seu email.
        """
        return db.query(User).filter(User.email == email).first()
    
    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """
        Cria um novo usuário no banco de dados.
        """
        user_data = obj_in.model_dump(exclude={"password"})
        hashed_password = get_password_hash(obj_in.password)
        db_obj = User(**user_data, hashed_password=hashed_password)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

# Instância única da classe para ser usada em toda a aplicação
user = CrudUser()