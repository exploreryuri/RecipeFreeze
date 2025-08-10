from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session
from app.models.user import User
from sqlalchemy import select
router = APIRouter()
@router.get("/users")
async def get_products(db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(User))
    return result.scalars().all()