from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    quantity = Column(Integer,String = False)
    products_id = Column(Integer,String = False)
    products = relationship("Product", back_populates="owner")