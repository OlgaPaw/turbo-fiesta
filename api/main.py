from typing import Dict, List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import auth, crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


# Dependency
def get_db() -> SessionLocal:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/larps/', response_model=schemas.Larp)
def create_larp(larp: schemas.Larp, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> models.Larp:
    return crud.create_larp(db=db, larp=larp)


@app.get('/larps/', response_model=List[schemas.LarpDetail])
def read_larps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[models.Larp]:
    larps = crud.get_larps(db, skip=skip, limit=limit)
    return larps


@app.get('/larps/{larp_id}', response_model=schemas.LarpDetail)
def read_larp(larp_id: int, db: Session = Depends(get_db)) -> models.Larp:
    db_larp = crud.get_larp(db, larp_id=larp_id)
    if db_larp is None:
        raise HTTPException(status_code=404, detail=f'Larp {larp_id} not found.')
    return db_larp


@app.post('/login', response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Dict:
    user = crud.get_user(db, form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail=f'Invalid login data.')
    if not auth.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail=f'Invalid login data.')
    token = auth.create_access_token(user.username)
    return {'access_token': token, 'token_type': 'bearer'}
