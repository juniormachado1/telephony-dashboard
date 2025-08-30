import httpx
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud, schemas
from app.core.config import settings

async def fetch_and_store_calls(db: Session) -> dict:
    """
    Busca dados da API de chamadas externa e os armazena no banco de dados.
    Evita a inserção de registros duplicados.
    """
    new_calls_count = 0
    updated_calls_count = 0 # Para futuras implementações de atualização

    # Cliente assíncrono para não bloquear a aplicação
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(settings.EXTERNAL_CALLS_API_URL, timeout=10.0)
            response.raise_for_status()  # Lança uma exceção para respostas 4xx/5xx
            external_calls = response.json()
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            print(f"Erro ao buscar dados da API externa: {e}")
            return {"error": "Falha ao se comunicar com a API externa."}


    # print("!!! ATENÇÃO: RODANDO EM MODO DE SIMULAÇÃO DE API !!!")
    # external_calls = [
    #     {
    #         "id": "mock_call_1",
    #         "timestamp": "2025-08-29T23:00:00Z",
    #         "source": "11999998888",
    #         "destination": "1133334444",
    #         "duration": 120,
    #         "sip_code": 200,
    #         "cost": 2.50
    #     },
    #     {
    #         "id": "mock_call_2",
    #         "timestamp": "2025-08-29T23:05:00Z",
    #         "source": "21888887777",
    #         "destination": "2144445555",
    #         "duration": 45,
    #         "sip_code": 486,
    #         "cost": 0.0
    #     }
    # ]


    for call_data in external_calls:
        # Verifica se a chamada já existe no banco
        existing_call = crud.call.get_by_call_id(db, call_id=call_data.get("id"))

        if not existing_call:
            """ 
            Validação Pydantic: garante que os dados externos
            se encaixam no nosso schema antes de salvar.
            """
            try:
                call_in = schemas.CallCreate(
                    call_id=call_data.get("id"),
                    call_date=datetime.fromisoformat(call_data.get("timestamp")),
                    source=call_data.get("source"),
                    destination=call_data.get("destination"),
                    duration=call_data.get("duration"),
                    sip_code=call_data.get("sip_code"),
                    cost=call_data.get("cost"),
                )
                crud.call.create(db, obj_in=call_in)
                new_calls_count += 1
            except Exception as e:
                # Logar falha de validação ou criação para um registro específico
                print(f"Não foi possível processar a chamada {call_data.get('id')}: {e}")

    return {"message": "Ingestão de dados concluída.", "new_calls": new_calls_count}
