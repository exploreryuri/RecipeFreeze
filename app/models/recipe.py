from sqlalchemy import Column, Integer, String
from database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    photo = Column(String, nullable=True)
    ingredients = Column(String)
    time = Column(Integer)
    difficulty = Column(String)
