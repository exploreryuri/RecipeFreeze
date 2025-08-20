from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from sqlalchemy import update, delete

def get_product_by_id(product_id: int, db: Session = Depends(get_db)) -> Product:
    result = db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

# CREATE
@router.post("/", response_model=ProductResponse)
def create_product(
    product_data: ProductCreate, 
    db: Session = Depends(get_db)
):
    new_product = Product(**product_data.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# READ (all)
@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    result = db.execute(select(Product))
    return result.scalars().all()

# READ (one)
@router.get("/{product_id}", response_model=ProductResponse)
def read_product(
    product_id: int, 
    db: Session = Depends(get_db)
):
    return get_product_by_id(db, product_id)

# UPDATE
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    product = get_product_by_id(db, product_id)
    
    update_data = product_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)
    
    db.commit()
    db.refresh(product)
    return product

# DELETE
@router.delete("/{product_id}")
async def delete_product(
    product_id: int, 
    db: Session = Depends(get_db)
):
    product = get_product_by_id(db, product_id)
    db.execute(delete(Product).where(Product.id == product_id))
    db.commit()
    return {"message": "Product deleted successfully"}