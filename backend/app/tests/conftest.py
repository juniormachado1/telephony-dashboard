import pytest
from typing import Generator, Dict
from sqlalchemy import create_engine, text 
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from app.main import app
from app.api import deps
from app.core.config import settings
from app.db.base import Base
from app import crud, schemas

# --- SETUP DO BANCO DE DADOS DE TESTE ---

default_engine = create_engine(str(settings.DATABASE_URL), isolation_level="AUTOCOMMIT")
test_engine = create_engine(str(settings.TEST_DATABASE_URL))
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    """
    Cria o banco de dados de teste antes de todos os testes
    e o destrói depois que todos terminam.
    """
    with default_engine.connect() as conn:
        db_name = settings.TEST_DATABASE_URL.split('/')[-1]
        # Envolve os comandos SQL com a função text()
        conn.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
        conn.execute(text(f"CREATE DATABASE {db_name}"))

    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

# --- FIXTURES PARA OS TESTES ---

@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture(scope="function")
def client(db_session: Session) -> Generator[TestClient, None, None]:
    def override_get_db() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[deps.get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    del app.dependency_overrides[deps.get_db]

@pytest.fixture(scope="function")
def superuser_token_headers(client: TestClient, db_session: Session) -> Dict[str, str]:
    email = "admin@test.com"
    password = "testpassword"

    user_in_db = crud.user.get_by_email(db=db_session, email=email)
    if not user_in_db:
        user_in = schemas.UserCreate(email=email, password=password, is_admin=True)
        crud.user.create(db=db_session, obj_in=user_in)

    login_data = {"username": email, "password": password}
    response = client.post("/api/v1/auth/login", data=login_data)
    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}
