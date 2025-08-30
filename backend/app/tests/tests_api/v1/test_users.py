from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import crud, schemas

def test_superuser_can_access_users_list(client: TestClient, superuser_token_headers: dict):
    """
    Testa se um superusuário autenticado pode acessar a lista de usuários.
    """
    response = client.get("/api/v1/users/", headers=superuser_token_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_normal_user_cannot_access_users_list(client: TestClient, db_session: Session):
    """
    Testa se um usuário comum recebe 403 Forbidden ao tentar listar usuários.
    """
    email = "normal.user@example.com"
    password = "userpassword"
    user_in = schemas.UserCreate(email=email, password=password, is_admin=False)
    crud.user.create(db=db_session, obj_in=user_in)
    
    login_response = client.post("/api/v1/auth/login", data={"username": email, "password": password})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/api/v1/users/", headers=headers)
    assert response.status_code == 403