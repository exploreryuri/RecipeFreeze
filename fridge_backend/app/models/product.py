from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    expiry_date = Column(DateTime(timezone=True), nullable=True)
    add_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    quantity = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


    owner = relationship("User", back_populates="products")
