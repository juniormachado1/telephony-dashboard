from pydantic import BaseModel, EmailStr
from typing import Optional

# Propriedades compartilhadas
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_admin: bool = False

# Propriedades para receber na criação
class UserCreate(UserBase):
    email: EmailStr
    password: str

# Propriedades para receber na atualização
class UserUpdate(UserBase):
    password: Optional[str] = None

# Propriedades armazenadas no DB
class UserInDBBase(UserBase):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

# Propriedades para retornar ao cliente
class User(UserInDBBase):
    pass