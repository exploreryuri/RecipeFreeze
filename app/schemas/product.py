from pydantic import BaseModel, validator
from typing import Optional, Literal

allowed_unit = ['г', 'кг', 'мл', 'л', 'шт', 'ст.л', 'ч.л']


class ProductBase(BaseModel):
    name: str
    quantity: int
    unit: Literal['г', 'кг', 'мл', 'л', 'шт', 'ст.л', 'ч.л']
    @validator('quantity')
    def check_products_not_null(cls, value):
        if value <= 0:
            raise ValueError("Quantity must be more than 0!")

    @validator('name')
    def check_products_not_null(cls, value):
        if value == '' or ' ':
            raise ValueError("Name must be not null")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: Optional[str]=None
    quantity: Optional[int]=None
    expiry_date: Optional[date]=None
    add_date: Optional[date]=None
    unit: Optional[Literal['г', 'кг', 'мл', 'л', 'шт', 'ст.л', 'ч.л']]=None
