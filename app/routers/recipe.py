from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from typing import List

from app.schemas.recipe import RecipeCreate, RecipeUpdate, RecipeResponse
from app.models.recipe import Recipe
from app.database import get_db

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"]
)

# @router.get("/recipes")
# def get_products(db: Session = Depends(get_db)):
#     result = db.execute(select(Recipe))
#     return result.scalars().all()

@router.post("/", response_model=RecipeResponse)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


@router.get("/", response_model=List[RecipeResponse])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    result = db.execute(select(Recipe).offset(skip).limit(limit))
    recipes = result.scalars().all()
    return recipes


@router.get("/{recipe_id}", response_model=RecipeResponse)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    result = db.execute(select(Recipe).filter(Recipe.id == recipe_id))
    db_recipe = result.scalars().first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe


@router.put("/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):
    result = db.execute(select(Recipe).filter(Recipe.id == recipe_id))
    db_recipe = result.scalars().first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    update_data = recipe.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_recipe, key, value)

    db.commit()
    db.refresh(db_recipe)
    return db_recipe


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    result = db.execute(select(Recipe).filter(Recipe.id == recipe_id))
    db_recipe = result.scalars().first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.execute(delete(Recipe).filter(Recipe.id == recipe_id))
    db.commit()
    return {"ok": True}