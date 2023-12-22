from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models, schemas


def create_room_type(request: schemas.RoomType, db: Session):
    room_type = models.RoomType(r_type=request.r_type, price=request.price)
    db.add(room_type)
    db.commit()
    db.refresh(room_type)

    return room_type


def create_room(request):
    pass
