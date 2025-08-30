from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import crud, schemas

def test_create_and_login_superuser(client: TestClient, db_session: Session):
    """
    Testa a criação de um superusuário e o subsequente login.
    """
    email = "test.admin@example.com"
    password = "testpassword"
    
    user_in = schemas.UserCreate(email=email, password=password, is_admin=True)
    user = crud.user.create(db=db_session, obj_in=user_in)
    assert user.email == email
    assert user.is_admin is True

    login_data = {"username": email, "password": password}
    response = client.post("/api/v1/auth/login", data=login_data)
    
    assert response.status_code == 200
    token = response.json()
    assert "access_token" in token
    assert token["token_type"] == "bearer"