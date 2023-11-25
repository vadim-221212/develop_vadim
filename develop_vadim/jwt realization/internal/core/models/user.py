# internal/models/user.py
from sqlalchemy import Column, String
from passlib.context import CryptContext
from internal.database import Base


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String),
    role = Column(String),
    email = Column(String)
    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)

