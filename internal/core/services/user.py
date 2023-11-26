# internal/services/user.py
from sqlalchemy.orm import Session
from internal.core.models.user import User


class UserService:
    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def create_user(self, db: Session, username: str, password: str, role: str):
        db_user = User(username=username, password=password, role=role)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


user_service = UserService()  # Создаем экземпляр UserService