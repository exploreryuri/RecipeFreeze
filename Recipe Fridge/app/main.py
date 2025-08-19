from fastapi import FastAPI
from app.routers import product, user, recipe
app = FastAPI()
app.include_router(product.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(recipe.router, prefix="/api")