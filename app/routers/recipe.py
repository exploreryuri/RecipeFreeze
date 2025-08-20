from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import List

from schemas.recipe import RecipeCreate, RecipeUpdate, RecipeResponse
from models.recipe import Recipe
from database import async_session

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"]
)

@router.get("/recipes")
async def get_products(db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Recipe))
    return result.scalars().all()
@router.post("/", response_model=RecipeResponse)
async def create_recipe(recipe: RecipeCreate, db: AsyncSession = Depends(async_session)):
    db_recipe = Recipe(**recipe.dict())
    db.add(db_recipe)
    await db.commit()
    await db.refresh(db_recipe)
    return db_recipe


@router.get("/", response_model=List[RecipeResponse])
async def read_recipes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Recipe).offset(skip).limit(limit))
    recipes = result.scalars().all()
    return recipes


@router.get("/{recipe_id}", response_model=RecipeResponse)
async def read_recipe(recipe_id: int, db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Recipe).filter(Recipe.id == recipe_id))
    db_recipe = result.scalars().first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe


@router.put("/{recipe_id}", response_model=RecipeResponse)
async def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Recipe).filter(Recipe.id == recipe_id))
    db_recipe = result.scalars().first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    update_data = recipe.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_recipe, key, value)

    await db.commit()
    await db.refresh(db_recipe)
    return db_recipe


@router.delete("/{recipe_id}")
async def delete_recipe(recipe_id: int, db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Recipe).filter(Recipe.id == recipe_id))
    db_recipe = result.scalars().first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    await db.execute(delete(Recipe).filter(Recipe.id == recipe_id))
    await db.commit()
    return {"ok": True}