from operator import index
from sqlalchemy import Boolean, Column, Float, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy.orm import backref, foreign, relationship


class RoomType(Base):
    __tablename__ = "roomtypes"

    id = Column(Integer, primary_key=True, index=True)
    r_type = Column(String)
    price = Column(Float)

    rooms = relationship("Room", back_populates="roomtype")


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    r_type_id = Column(Integer, ForeignKey("roomtypes.id"))
    room_no = Column(Integer)
    available = Column(Boolean, default=True)

    roomtype = relationship("RoomType", back_populates="rooms")
    record = relationship("Record", back_populates="room")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    nrc_id = Column(String, unique=True)
    name = Column(String)

    record = relationship("Record", back_populates="customer")


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    checkin = Column(DateTime, server_default=func.now())
    checkout = Column(DateTime, server_default=func.now(), onupdate=func.now())

    customer = relationship("Customer", back_populates="records")
    room = relationship("Room", back_populates="records")


"""
what if i create a record with customer name !!!
that might be more efficient
but a  nrc id may not be unique !
"""
