from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.models.user import User
from app.services import metrics_service

router = APIRouter()

@router.get("/", response_model=schemas.MetricsResponse)
def read_metrics(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Recupera os KPIs e dados para o gráfico do dashboard.
    Acessível por qualquer usuário logado.
    """
    metrics = metrics_service.get_metrics(db)
    return metrics