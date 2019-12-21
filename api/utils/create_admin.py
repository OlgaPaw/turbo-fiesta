from argparse import ArgumentParser
from contextlib import contextmanager

from sqlalchemy.orm.session import Session

from api import auth, crud, database, models, schemas


def create_user(db: Session, username: str, password: str) -> models.User:
    password_hash = auth.get_password_hash(password)
    user = schemas.User(username=username, password_hash=password_hash)
    existing_user = crud.get_user(db, username)
    if existing_user:
        print(f'Updating user {username}')
        return crud.update_user(db, existing_user.id, user)
    else:
        print(f'Adding user {username}')
        return crud.create_user(db, user)


@contextmanager
def get_db() -> database.SessionLocal:
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    parser = ArgumentParser(description='Script to add user.')
    parser.add_argument('--password', '-p', type=str, help='password')
    parser.add_argument('--user', '-u', type=str, help='user name')
    args = parser.parse_args()

    with get_db() as db:
        create_user(db, args.user, args.password)
