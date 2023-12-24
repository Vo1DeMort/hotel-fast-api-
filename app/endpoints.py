from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import schema
from sqlalchemy.sql.compiler import crud
from . import schemas, database, models
from sqlalchemy.orm import Session
from . import CRUDs

router = APIRouter()

get_db = database.get_db

""" i need better understanding of these codes """


# create_room_type
@router.post("/create_room_type", status_code=status.HTTP_201_CREATED)
def create_room_type(request: schemas.RoomType, db: Session = Depends(get_db)):
    return CRUDs.create_room_type(request, db)


# get RoomType
@router.get("/get_roomtypes", response_model=List[schemas.ResponseRoomType])
def get_roomtypes(db: Session = Depends(get_db)):
    return CRUDs.get_room_types(db)


@router.post("/create_room", status_code=status.HTTP_201_CREATED)
def create_room(request: schemas.Room, db: Session = Depends(get_db)):
    return CRUDs.create_room(request, db)


@router.get("/available_rooms", response_model=List[schemas.Room])
def available_rooms(db: Session = Depends(get_db)):
    return CRUDs.get_available_rooms(db)


@router.post("/create_customer", status_code=status.HTTP_201_CREATED)
def create_customer(request: schemas.Customer, db: Session = Depends(get_db)):
    return CRUDs.create_customer(request, db)


""" have not test the record post and update yet """


@router.post("/create_record", status_code=status.HTTP_201_CREATED)
def create_record(request: schemas.Record, db: Session = Depends(get_db)):
    return CRUDs.create_record(request, db)


@router.put("/records/{record_id}/update_checkout")
def update_record_checkout(record_id: int, db: Session = Depends(get_db)):
    record = CRUDs.update_record(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record
