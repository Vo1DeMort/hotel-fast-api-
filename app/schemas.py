from pydantic import BaseModel


class Customer(BaseModel):
    nrc_id: str
    name: str


class RoomType(BaseModel):
    r_type: str
    price: float


class Room(BaseModel):
    no: int
    available: bool
