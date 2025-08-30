from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud,schemas
from app.models.user import User
from app.api import deps
from app.services import call_service

router = APIRouter()

@router.get("/", response_model=List[schemas.Call])
def read_calls(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Recupera uma lista de chamadas do banco de dados.
    Acessível por qualquer usuário logado.
    """
    calls = crud.call.get_multi(db, skip=skip, limit=limit)
    return calls

@router.post("/ingest", response_model=schemas.Msg)
async def ingest_calls_from_api(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Explicação: Em um sistema de produção, isso seria um background job agendado (ex: Celery, ARQ),
    não um endpoint de API. Para este case, um acionador manual é suficiente.
    """
    result = await call_service.fetch_and_store_calls(db)
    if "error" in result:
         return {"msg": result["error"]}
    return {"msg": f"Ingestão concluída! Novas chamadas: {result.get('new_calls', 0)}"}
