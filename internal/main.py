from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from internal.core.services.auth.jwt import decode_access_token
from internal.core.models.user import User
from internal.config import settings
from pydantic import BaseModel
from jose import JWTError, jwt
from internal.core.services.user import user_service



app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData(BaseModel):
   username: str

@app.get("/users/me")
async def read_current_user(token: str = Depends(oauth2_scheme), current_user: User = Depends(decode_access_token)):
   credentials_exception = HTTPException(
       status_code=401,
       detail="Could not validate credentials",
       headers={"WWW-Authenticate": "Bearer"},
   )
   try:
       payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
       username: str = payload.get("sub")
       if username is None:
           raise credentials_exception
       token_data = TokenData(username=username)
   except JWTError:
       raise credentials_exception

   user = user_service.get_user_by_username(db, username=token_data.username)
   if user is None:
       raise credentials_exception

   return user
