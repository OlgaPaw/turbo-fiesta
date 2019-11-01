from datetime import datetime

from pydantic import UrlStr, BaseModel


class Larp(BaseModel):
    name: str
    organizer: str
    datetime_start: datetime
    datetime_end: datetime
    website: UrlStr = None
    image: UrlStr = None
    description: str = None

    class Config:
        orm_mode = True


class LarpDetail(Larp):
    id: int
    validated: bool
