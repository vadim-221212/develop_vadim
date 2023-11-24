# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from internal.services.auth.jwt import get_current_user
from internal.models.user import User

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
async def read_current_user(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "email": current_user.email}
