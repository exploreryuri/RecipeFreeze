from sqlalchemy import Column, Integer, String
from app.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    difficulty = Column(Integer, default=1)