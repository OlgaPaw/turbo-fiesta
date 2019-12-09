from typing import List

from sqlalchemy.orm import Session

from . import models, schemas


def get_larp(db: Session, larp_id: int) -> models.Larp:
    return db.query(models.Larp).filter(models.Larp.id == larp_id).first()


def get_larps(db: Session, skip: int = 0, limit: int = 100) -> List[models.Larp]:
    return db.query(models.Larp).offset(skip).limit(limit).all()


def create_larp(db: Session, larp: schemas.Larp) -> models.Larp:
    db_larp = models.Larp(**larp.dict())
    db.add(db_larp)
    db.commit()
    db.refresh(db_larp)
    return db_larp


def get_user(db: Session, user_name: int) -> models.User:
    return db.query(models.User).filter(models.User.username == user_name).first()


def create_user(db: Session, user: schemas.User) -> models.User:
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
