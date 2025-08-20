# app/schemas/recipe.py
from pydantic import BaseModel, validator
from typing import Optional

class RecipeBase(BaseModel):
    name: str
    photo: Optional[str] = None
    ingredients: str  # Пока строка, позже можно заменить на список/сущности
    time: int
    difficulty: str

    @validator('time')
    def check_time_non_negative(cls, value):
        if value < 0:
            raise ValueError('Time must be non-negative')
        return value

    @validator('difficulty')
    def check_difficulty(cls, value):
        valid_difficulties = ['easy', 'medium', 'hard']
        if value not in valid_difficulties:
            raise ValueError(f'Difficulty must be one of: {", ".join(valid_difficulties)}')
        return value

class RecipeCreate(RecipeBase):
    pass  # Все поля из RecipeBase, photo уже опционально

class RecipeUpdate(BaseModel):
    name: Optional[str] = None
    photo: Optional[str] = None
    ingredients: Optional[str] = None
    time: Optional[int] = None
    difficulty: Optional[str] = None

    @validator('time', allow_reuse=True)
    def check_time_non_negative(cls, value):
        if value is not None and value < 0:
            raise ValueError('Time must be non-negative')
        return value

    @validator('difficulty', allow_reuse=True)
    def check_difficulty(cls, value):
        if value is not None:
            valid_difficulties = ['easy', 'medium', 'hard']
            if value not in valid_difficulties:
                raise ValueError(f'Difficulty must be one of: {", ".join(valid_difficulties)}')
            return value

class RecipeResponse(RecipeBase):
    id: int

    class Config:
        from_attributes = True