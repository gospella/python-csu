from fastapi.testclient import TestClient
from main import app
from db.models import User, UserInfo

client = TestClient(app)


def test_form(db, user):
    test_user = (
        db.query(UserInfo)
        .join(User, UserInfo.user_id == User.id)
        .filter(User.username == user.username, User.password == user.password)
        .one_or_none()
    )
    assert test_user.name == "Тестовый админ"
