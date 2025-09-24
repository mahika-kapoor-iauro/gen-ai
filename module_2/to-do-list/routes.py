from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Task, User
from database import SessionLocal
from auth import get_current_user, get_password_hash, create_access_token, authenticate_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
async def register(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(SessionLocal)):
    user = await db.execute(select(User).where(User.username == form_data.username))
    if user.scalars().first():
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(username=form_data.username, hashed_password=get_password_hash(form_data.password))
    db.add(new_user)
    await db.commit()
    return {"msg": "User registered"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(SessionLocal)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/tasks")
async def get_tasks(db: AsyncSession = Depends(SessionLocal), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Task).where(Task.owner_id == current_user.id))
    return result.scalars().all()

@router.post("/tasks")
async def create_task(title: str, db: AsyncSession = Depends(SessionLocal), current_user: User = Depends(get_current_user)):
    task = Task(title=title, owner_id=current_user.id)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, completed: bool, db: AsyncSession = Depends(SessionLocal), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Task).where(Task.id == task_id, Task.owner_id == current_user.id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = completed
    await db.commit()
    await db.refresh(task)
    return task
