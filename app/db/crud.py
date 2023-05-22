from sqlalchemy.orm import Session
from db.models import UserInfo, User

def check_user_auth(db: Session, username: str, password: str):
    return (
        db.query(UserInfo)
        .join(User, UserInfo.user_id == User.id)
        .filter(User.username == username, User.password == password)
        .one_or_none()
    )