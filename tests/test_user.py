from lib.user import User
import hashlib

def test_constructs():
    user = User(1, 'user@test.com', 'password123!', 'Test User', 'test_user')
    assert user.id == 1
    assert user.name == 'Test User'
    assert user.username == 'test_user'
    assert user._email == "user@test.com"
    assert user._password == 'password123!'

def test_formatting():
    user = User(1, 'user@test.com', 'password123!', 'Test User', 'test_user')
    assert str(user) == 'User(1, Test User, test_user)'

def test_equality():
    user_1 = User(1, 'user@test.com', 'password123!', 'Test User', 'test_user')
    user_2 = User(1, 'user@test.com', 'password123!', 'Test User', 'test_user')
    assert user_1 == user_2

def test_user_missing_fields():
    assert User(1, "", "", "", "").is_valid() == False
    assert User(1, "user@test.com", "", "", "").is_valid() == False
    assert User(1, "", "password123!", "", "").is_valid() == False
    assert User(1, "", "", "Test User", "").is_valid() == False
    assert User(1, "", "", "", "test_user").is_valid() == False
    assert User(1, "user@test.com", "password123!", "", "").is_valid() == False
    assert User(1, "user@test.com", "", "Test User", "").is_valid() == False
    assert User(1, "user@test.com", "", "", "test_user").is_valid() == False
    assert User(1, "", "password123!", "Test User", "").is_valid() == False
    assert User(1, "", "password123!", "", "test_user").is_valid() == False
    assert User(1, "", "", "Test User", "test_user").is_valid() == False
    assert User(1, "user@test.com", "password123!", "Test User", "").is_valid() == False
    assert User(1, "user@test.com", "", "Test User", "test_user").is_valid() == False
    assert User(1, "", "password123!", "Test User", "test_user").is_valid() == False
    assert User(1, "user@test.com", "password123!", "", "test_user").is_valid() == False
    assert User(1, "user@test.com", "password123!", "Test User", "test_user").is_valid() == True
    assert User(None, "user@test.com", "password123!", "Test User", "test_user").is_valid() == True

def test_user_invalid_email():
    assert User(1, "user.com", "password123!", "Test User", "test_user").is_valid() == False
    assert User(1, "example@test", "password123!", "Test User", "test_user").is_valid() == False
    assert User(1, "user@test.com", "password123!", "Test User", "test_user").is_valid() == True
    assert User(1, "user@test.co.uk", "password123!", "Test User", "test_user").is_valid() == True
    
def test_user_invalid_password():
    assert User(1, "user@test.com", "test", "Test User", "test_user").is_valid() == False
    assert User(1, "user@test.com", "test!", "Test User", "test_user").is_valid() == False
    assert User(1, "user@test.com", "password123", "Test User", "test_user").is_valid() == False
    assert User(1, "user@test.com", "password123!", "Test User", "test_user").is_valid() == True

def test_user_errors():
    assert User(1, "", "", "", "").generate_errors() == "Email can't be blank, Password can't be blank, Name can't be blank, Username can't be blank"

def test_invalid_email_error():
    assert User(1, "user.com", "password123!", "Test User", "test_user").generate_errors() == "Invalid email"
    assert User(1, "example@test", "password123!", "Test User", "test_user").generate_errors() == "Invalid email"
    assert User(1, "user@test.com", "password123!", "Test User", "test_user").generate_errors() == None
    assert User(1, "user@test.co.uk", "password123!", "Test User", "test_user").generate_errors() == None

def test_user_invalid_password_error():
    assert User(1, "user@test.com", "test", "Test User", "test_user").generate_errors() == "Password must be at least 8 characters long, Password must have at least 1 special character"
    assert User(1, "user@test.com", "test!", "Test User", "test_user").generate_errors() == "Password must be at least 8 characters long"
    assert User(1, "user@test.com", "password123", "Test User", "test_user").generate_errors() == "Password must have at least 1 special character"
    assert User(1, "user@test.com", "password123!", "Test User", "test_user").generate_errors() == None