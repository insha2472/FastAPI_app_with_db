from fastapi import APIRouter

router = APIRouter()

@router.get("/signup")
def signup():
    return {"message": "user created"}

@router.get("/login")
def login():
    return {"message": "user logged in successfully"} 
    