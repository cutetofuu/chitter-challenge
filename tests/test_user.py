from lib.user import User

def test_constructs():
    user = User(1, 'user@test.com', 'password123', 'Test User', 'test_user')
    assert user.id == 1
    assert user.email == 'user@test.com'
    assert user.password == 'password123'
    assert user.name == 'Test User'
    assert user.username == 'test_user'

def test_formatting():
    user = User(1, 'user@test.com', 'password123', 'Test User', 'test_user')
    assert str(user) == 'User(1, user@test.com, password123, Test User, test_user)'

def test_equality():
    user_1 = User(1, 'user@test.com', 'password123', 'Test User', 'test_user')
    user_2 = User(1, 'user@test.com', 'password123', 'Test User', 'test_user')
    assert user_1 == user_2