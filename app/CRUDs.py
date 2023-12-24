from operator import mod
import re
from pydantic_core.core_schema import custom_error_schema
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models, schemas


def create_room_type(request: schemas.RoomType, db: Session):
    room_type = models.RoomType(r_type=request.r_type, price=request.price)
    db.add(room_type)
    db.commit()
    db.refresh(room_type)

    return room_type


def get_room_types(db: Session):
    room_types = db.query(models.RoomType).all()
    return room_types


def create_room(request: schemas.Room, db: Session):
    room = models.Room(
        r_type_id=request.r_type_id,
        room_no=request.room_no,
    )
    db.add(room)
    db.commit()
    db.refresh(room)

    return room


def get_available_rooms(db: Session):
    rooms = db.query(models.Room).filter(models.Room.available == True).all()
    return rooms


def create_customer(request: schemas.Customer, db: Session):
    # a littel check if the customer is already existed in the db
    old_customer = (
        db.query(models.Customer)
        .filter(models.Customer.nrc_id == request.nrc_id)
        .first()
    )

    if not old_customer:
        customer = models.Customer(nrc_id=request.nrc_id, name=request.name)
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    else:
        return {"customer already exist ": old_customer}


def create_record(request: schemas.Record, db: Session):
    record = models.Record(customer_id=request.customer_id, room_id=request.room_id)
    db.add(record)
    db.commit()
    db.refresh(record)

    return record
