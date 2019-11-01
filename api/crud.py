from sqlalchemy.orm import Session

from . import models, schemas


def get_larp(db: Session, larp_id: int):
    return db.query(models.Larp).filter(models.Larp.id == larp_id).first()


def get_larps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Larp).offset(skip).limit(limit).all()


def create_larp(db: Session, larp: schemas.Larp):
    db_larp = models.Larp(**larp.dict())
    db.add(db_larp)
    db.commit()
    db.refresh(db_larp)
    return db_larp
