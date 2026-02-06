from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositeries.user_repo import UserRepo
from schemas.user_schemas import UserSchema

router = APIRouter()

@router.get("/signup")
def signup(db:Session=Depends(get_db)):
    user_repo = UserRepo(db)
    user_repo.add_user(user)
    return {"message": "user created"}

@router.get("/login")
def login():
    return {"message": "user logged in successfully"} 
    