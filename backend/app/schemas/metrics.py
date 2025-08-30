from pydantic import BaseModel
from datetime import date

class KPIs(BaseModel):
    total_calls: int = 0
    answered_calls: int = 0
    asr: float = 0.0  # Answer Seizure Ratio, em porcentagem
    acd: float = 0.0  # Average Call Duration, em segundos

class ChartDataPoint(BaseModel):
    time_point: str # Ex: "2025-08-29 23:00" ou "2025-08-29"
    total_calls: int

class MetricsResponse(BaseModel):
    kpis: KPIs
    chart_data: list[ChartDataPoint]
    