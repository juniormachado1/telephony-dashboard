from fastapi.testclient import TestClient
from app.models.call import Call
from sqlalchemy.orm import Session

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.call import Call

def test_ingest_calls_mocked(client: TestClient, superuser_token_headers: dict, db_session: Session, mocker):
    """
    Testa o endpoint de ingestão, simulando a resposta da API externa.
    """
    db_session.query(Call).delete()
    db_session.commit()

    # Mock da chamada HTTP para a API externa com 2 chamadas
    mock_data = [
        {"id": "test_call_1", "timestamp": "2025-01-01T12:00:00Z", "source": "1", "destination": "2", "duration": 60, "sip_code": 200, "cost": 1.0},
        {"id": "test_call_2", "timestamp": "2025-01-01T13:00:00Z", "source": "3", "destination": "4", "duration": 120, "sip_code": 200, "cost": 2.0}
    ]
    mocker.patch("app.services.call_service.httpx.AsyncClient.get").return_value.json.return_value = mock_data
    mocker.patch("app.services.call_service.httpx.AsyncClient.get").return_value.raise_for_status.return_value = None

    # Executa a ingestão
    response = client.post("/api/v1/calls/ingest", headers=superuser_token_headers)

    expected_msg = "Ingestão concluída! Novas chamadas: 2"
    assert response.status_code == 200
    assert response.json()["msg"] == expected_msg

    # Verifica se as chamadas foram salvas no banco
    calls_in_db = db_session.query(Call).count()
    assert calls_in_db == 2