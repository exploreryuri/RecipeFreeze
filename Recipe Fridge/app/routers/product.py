from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session
from app.models.product import Product
from sqlalchemy import select
router = APIRouter()
@router.get("/product")
async def get_products(db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Product))
    return result.scalars().all()
