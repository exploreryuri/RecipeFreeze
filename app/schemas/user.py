from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """Базовая схема пользователя"""
    username: str = Field(..., min_length=3, max_length=50, example="john_doe")
    email: EmailStr = Field(..., example="user@example.com")
    full_name: Optional[str] = Field(None, max_length=100, example="John Doe")

class UserCreate(UserBase):
    """Схема для создания пользователя"""
    password: str = Field(..., min_length=6, max_length=100, example="strongpassword")

class UserUpdate(BaseModel):
    """Схема для обновления пользователя"""
    email: Optional[EmailStr] = Field(None, example="new_email@example.com")
    full_name: Optional[str] = Field(None, max_length=100, example="New Name")
    password: Optional[str] = Field(None, min_length=6, max_length=100, example="newpassword")

class UserInDB(UserBase):
    """Схема пользователя в БД"""
    id: int
    hashed_password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Ранее known as orm_mode

class UserResponse(UserBase):
    """Схема для ответа API"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True