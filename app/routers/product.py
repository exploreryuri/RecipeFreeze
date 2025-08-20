from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import async_session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from sqlalchemy import update, delete

async def get_product_by_id(db: AsyncSession, product_id: int) -> Product:
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

@router.get("/products")
async def get_products(db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Product))
    return result.scalars().all()

# CREATE
@router.post("/", response_model=ProductResponse)
async def create_product(
    product_data: ProductCreate, 
    db: AsyncSession = Depends(async_session)
):
    new_product = Product(**product_data.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

# READ (all)
@router.get("/", response_model=List[ProductResponse])
async def read_products(db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Product))
    return result.scalars().all()

# READ (one)
@router.get("/{product_id}", response_model=ProductResponse)
async def read_product(
    product_id: int, 
    db: AsyncSession = Depends(async_session)
):
    return await get_product_by_id(db, product_id)

# UPDATE
@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int, 
    product_data: ProductUpdate, 
    db: AsyncSession = Depends(async_session)
):
    product = await get_product_by_id(db, product_id)
    
    update_data = product_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)
    
    await db.commit()
    await db.refresh(product)
    return product

# DELETE
@router.delete("/{product_id}")
async def delete_product(
    product_id: int, 
    db: AsyncSession = Depends(async_session)
):
    product = await get_product_by_id(db, product_id)
    await db.execute(delete(Product).where(Product.id == product_id))
    await db.commit()
    return {"message": "Product deleted successfully"}