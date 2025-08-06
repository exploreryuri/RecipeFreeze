from sqlalchemy import Column, Integer, String
from app.database import Base

class Recipe(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    time = Column(String, nullable=False)
    dificulty = Column(Integer, String=False)