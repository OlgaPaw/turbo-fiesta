from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UrlStr


class Larp(BaseModel):
    name: str
    organizer: str
    datetime_start: datetime
    datetime_end: datetime
    website: UrlStr = None
    image: UrlStr = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class LarpDetail(Larp):
    id: int
    validated: bool
