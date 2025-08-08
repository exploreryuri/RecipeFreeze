from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel
from typing import Optional

# ====================== Настройка БД ======================
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Исправленная строка - новый стиль SQLAlchemy 2.0
Base = declarative_base()

# ====================== Модель Product ======================
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String, nullable=True)

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# ====================== Pydantic схемы ======================
class ProductBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True  # Для совместимости с SQLAlchemy

# ====================== FastAPI приложение ======================
app = FastAPI()

# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====================== CRUD операции ======================
@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products/", response_model=list[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, 
    product: ProductCreate, 
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for field, value in product.model_dump().items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
