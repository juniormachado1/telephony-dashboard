from pydantic import BaseModel
from datetime import datetime

# Propriedades base da chamada
class CallBase(BaseModel):
    call_id: str
    call_date: datetime
    source: str
    destination: str
    duration: int
    sip_code: int
    cost: float

# Schema para criar uma chamada no DB (herdando da base)
class CallCreate(CallBase):
    pass

# Schema para ler uma chamada do DB (retornar na API)
class Call(CallBase):
    id: int

    class Config:
        from_attributes = True