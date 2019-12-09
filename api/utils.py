from datetime import date

from sqlalchemy.orm.session import Session

from . import auth, crud, models, schemas


def create_admin(db: Session) -> models.User:
    password = 'admin' + date.today().isoformat()
    password_hash = auth.get_password_hash(password)
    admin = schemas.User(username='admin', password_hash=password_hash)
    return crud.create_user(db, admin)
