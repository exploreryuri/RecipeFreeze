from pydantic import BaseModel

class RecipeBase(BaseModel):
    name: str
    photo: str
    ingredients: str
    time: int
    difficulty: str

class RecipeCreate(RecipeBase):
    pass

class RecipeResponse(RecipeBase):
    id: int
    class Config:
        orm_mode = True
