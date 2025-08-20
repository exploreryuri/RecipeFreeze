from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "postgresql+psycopg2://postgres:2202@localhost:5432/fridge_db"

Base = declarative_base()
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    pool_recycle=1800,
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db: Session = async_session
    try:
        yield db
    finally:
        db.close()