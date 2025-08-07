from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_session
from user import User
from sqlalchemy.future import select

router = APIRouter()

@router.get("/products")
async def get_products(db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(User))
    return result.scalars().all()
