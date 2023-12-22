from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.sql.compiler import crud
from . import schemas, database, models
from sqlalchemy.orm import Session
from . import CRUDs

router = APIRouter()

get_db = database.get_db

""" i need better understanding of these codes """


@router.post("/create_room_type", status_code=status.HTTP_201_CREATED)
def create_room_type(request: schemas.RoomType, db: Session = Depends(get_db)):
    return CRUDs.create_room_type(request, db)
