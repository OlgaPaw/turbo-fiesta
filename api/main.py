from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db() -> SessionLocal:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/larps/', response_model=schemas.Larp)
def create_larp(larp: schemas.Larp, db: Session = Depends(get_db)) -> models.Larp:
    return crud.create_larp(db=db, larp=larp)


@app.get('/larps/', response_model=List[schemas.LarpDetail])
def read_larps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[models.Larp]:
    larps = crud.get_larps(db, skip=skip, limit=limit)
    return larps


@app.get('/larps/{larp_id}', response_model=schemas.LarpDetail)
def read_larp(larp_id: int, db: Session = Depends(get_db)) -> models.Larp:
    db_larp = crud.get_larp(db, larp_id=larp_id)
    if db_larp is None:
        raise HTTPException(status_code=404, detail=f'Larp {larp_id} not found')
    return db_larp
