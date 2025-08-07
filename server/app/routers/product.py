from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_session
from product import Product

router = APIRouter()

@router.get("/products")
async def get_products(db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Product))
    return result.scalars().all()
