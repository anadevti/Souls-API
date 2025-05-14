# app/models/game.py
from sqlalchemy import Column, Integer, String, Text, Date
from app.db.base import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    release_date = Column(Date, nullable=True)
    description = Column(Text, nullable=True)