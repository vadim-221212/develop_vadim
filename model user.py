# internal/models/user.py
from sqlalchemy import Column, String
from internal.database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password = Column(String)
    role = Column(String)
    email = Column(String)
