from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True
