from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Cria o engine do banco com verificação automática de conexões ativas.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Cria sessões do banco com controle manual de transações e sem autoflush automático.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)