from pydantic import BaseModel
from datetime import datetime


class RoomType(BaseModel):
    r_type: str
    price: float


class ResponseRoomType(RoomType):
    id: int

    class Config:
        # convert sqlalchemy models to pydantic model
        orm_mode = True


class Room(BaseModel):
    r_type_id: int
    room_no: int
    available: bool


class Customer(BaseModel):
    nrc_id: str
    name: str


class Record(BaseModel):
    customer_id: int
    room_id: int
    checkin: datetime
    checkout: datetime
