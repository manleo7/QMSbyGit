from fastapi import APIRouter, Depends, HTTPException
from app.auth.utils import verify_password, get_password_hash, create_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session
from app.models.user import User
from sqlalchemy.future import select
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str
    email: str

@router.post("/register")
async def register(user: UserCreate, session: AsyncSession = Depends(async_session)):
    user_obj = User(
        username=user.username,
        hashed_password=get_password_hash(user.password),
        full_name=user.full_name,
        email=user.email
    )
    session.add(user_obj)
    await session.commit()
    await session.refresh(user_obj)
    return {"msg": "User registered"}

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(user: UserLogin, session: AsyncSession = Depends(async_session)):
    result = await session.execute(select(User).where(User.username == user.username))
    user_obj = result.scalar_one_or_none()
    if not user_obj or not verify_password(user.password, user_obj.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user_obj.username})
    return {"access_token": token, "token_type": "bearer"}