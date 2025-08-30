from sqlalchemy.orm import Session
from app import crud, schemas

def get_metrics(db: Session) -> schemas.MetricsResponse:
    """
    Busca os dados do CRUD e calcula as métricas para a resposta da API.
    """
    # 1. Obter dados brutos do CRUD
    kpi_data = crud.call.get_kpi_data(db)
    total_calls = kpi_data.get("total_calls", 0)
    answered_calls = kpi_data.get("answered_calls", 0)
    total_duration_answered = kpi_data.get("total_duration_answered", 0)

    # 2. Calcular métricas derivadas
    # ASR: (Atendidas / Total) * 100. Cuidar da divisão por zero.
    asr = (answered_calls / total_calls * 100) if total_calls > 0 else 0.0
    # ACD: Duração Total / Atendidas. Cuidar da divisão por zero.
    acd = (total_duration_answered / answered_calls) if answered_calls > 0 else 0.0

    kpis = schemas.KPIs(
        total_calls=total_calls,
        answered_calls=answered_calls,
        asr=round(asr, 2), # Arredonda para 2 casas decimais
        acd=round(acd, 2)
    )

    # 3. Obter e formatar dados do gráfico
    chart_data_raw = crud.call.get_chart_data(db)
    chart_data = [
        schemas.ChartDataPoint(
            time_point=row.time_point.strftime("%Y-%m-%d %H:%M"),
            total_calls=row.total_calls
        )
        for row in chart_data_raw
    ]

    # 4. Montar e retornar a resposta final
    return schemas.MetricsResponse(kpis=kpis, chart_data=chart_data)
