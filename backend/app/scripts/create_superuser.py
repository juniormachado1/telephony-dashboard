import argparse

from app.db.session import SessionLocal
from app import crud, schemas

def main() -> None:
    parser = argparse.ArgumentParser(description="Create a superuser.")
    parser.add_argument("email", type=str, help="The user's email")
    parser.add_argument("password", type=str, help="The user's password")
    args = parser.parse_args()

    db = SessionLocal()

    user_in_db = crud.user.get_by_email(db, email=args.email)
    if user_in_db:
        print(f"User with email {args.email} already exists.")
        return

    user_in = schemas.UserCreate(
        email=args.email,
        password=args.password,
        is_admin=True
    )
    new_user = crud.user.create(db, obj_in=user_in)
    print(f"Superuser {new_user.email} created successfully.")

if __name__ == "__main__":
    main()