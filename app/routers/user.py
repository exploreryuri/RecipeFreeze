from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Создание пользователя
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Проверка на уникальность username и email
    db_user = db.query(User).filter(
        (User.username == user.username) | 
        (User.email == user.email)
    ).first()
    
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,  # Без шифрования!
        full_name=user.full_name
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Получение пользователя по ID
@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

# Получение всех пользователей
@router.get("/", response_model=list[UserResponse])
def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

# Обновление пользователя
@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int, 
    user_data: UserUpdate, 
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    update_data = user_data.model_dump(exclude_unset=True)
    
    # Проверка на уникальность email при обновлении
    if 'email' in update_data:
        existing_user = db.query(User).filter(
            User.email == update_data['email'],
            User.id != user_id
        ).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    for field, value in update_data.items():
        setattr(user, field, value)
    
    db.commit()
    db.refresh(user)
    return user

# Удаление пользователя
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    db.delete(user)
    db.commit()
    return None
