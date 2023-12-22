from sqlalchemy import Column, Float, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class RoomType(Base):
    __tablename__ = "roomtypes"

    id = Column(Integer, primary_key=True, index=True)
    r_type = Column(String)
    price = Column(Float)
