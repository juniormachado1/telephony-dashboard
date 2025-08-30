from sqlalchemy import Column, Integer, String, DateTime, Float
from app.db.base import Base

class Call(Base):
    """
    Representa uma chamada telefônica registrada no sistema, 
    com dados como origem, destino, duração e custo.
    """
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String, unique=True, index=True) # ID da chamada da API externa
    call_date = Column(DateTime, index=True)
    source = Column(String, index=True)
    destination = Column(String, index=True)
    duration = Column(Integer) # Duração em segundos
    sip_code = Column(Integer, index=True)
    cost = Column(Float)
    