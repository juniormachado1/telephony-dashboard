from fastapi.testclient import TestClient
from app.models.call import Call
from sqlalchemy.orm import Session
from datetime import datetime

def test_metrics_calculation(client: TestClient, db_session: Session, superuser_token_headers: dict):
    """
    Testa se o endpoint de métricas calcula os KPIs corretamente.
    """
    db_session.query(Call).delete() # Limpa chamadas de testes anteriores
    db_session.add_all([
        Call(call_id="m1", call_date=datetime.now(), source="a", destination="b", duration=100, sip_code=200, cost=1),
        Call(call_id="m2", call_date=datetime.now(), source="c", destination="d", duration=200, sip_code=200, cost=2),
        Call(call_id="m3", call_date=datetime.now(), source="e", destination="f", duration=50, sip_code=486, cost=0),
        Call(call_id="m4", call_date=datetime.now(), source="g", destination="h", duration=20, sip_code=404, cost=0)
    ])
    db_session.commit()
    
    response = client.get("/api/v1/metrics/", headers=superuser_token_headers)
    assert response.status_code == 200
    kpis = response.json()["kpis"]
    
    assert kpis["total_calls"] == 4
    assert kpis["answered_calls"] == 2
    assert kpis["asr"] == 50.0
    assert kpis["acd"] == 150.0