import pytest
from db import init_db, insert_user, get_users, update_user, delete_user

@pytest.fixture(scope="module")
def setup_db():
    """Ініціалізує БД перед тестами"""
    init_db()

def test_insert_user(setup_db):
    """Тестує вставку користувача"""
    user_id = insert_user("John Doe", 30)
    assert user_id is not None

def test_get_users(setup_db):
    """Тестує вибірку користувачів"""
    users = get_users()
    assert len(users) > 0

def test_update_user(setup_db):
    """Тестує оновлення даних користувача"""
    users = get_users()
    user_id = users[0][0]
    update_user(user_id, "Jane Doe", 25)
    updated_user = get_users()[0]
    assert updated_user[1] == "Jane Doe"
    assert updated_user[2] == 25

def test_delete_user(setup_db):
    """Тестує видалення користувача"""
    users = get_users()
    user_id = users[0][0]
    delete_user(user_id)
    users_after_delete = get_users()
    assert len(users_after_delete) == 0
