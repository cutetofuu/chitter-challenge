from lib.user_repository import UserRepository
from lib.user import User
import hashlib

def test_all(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.all()
    assert result == [
        User(1, 'david@test.com', '40ccbdf74ca095cbf6a05ede129d3aebdaa16e799b5897be82ca0948fd995d20', 'David', 'dave_test'),
        User(2, 'jane@test.com', '74003ee4634d383f4a1921d434f16e6ef14e2a3259246c130e8a31055250635e', 'Jane', 'jane_test'),
        User(3, 'pickle@test.com', '7052d09741567eaa79757c241d3ee5e2022ad63690ef0f3b2e02f62d5ca6cf6e', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'c6e8b79a09af0a5955447f0fc10348e911a867d11aa4505d411081ace5aa4298', 'John', 'john_test')
    ]

def test_find(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.find(3)
    assert result == User(3, 'pickle@test.com', '7052d09741567eaa79757c241d3ee5e2022ad63690ef0f3b2e02f62d5ca6cf6e', 'Pickle', 'pickle_test')

def test_create(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    user = User(None, 'someone@test.com', 'password999!', 'Someone', 'someone_test')
    repo.create(user)

    binary_password = 'password999!'.encode("utf-8")
    hashed_password = hashlib.sha256(binary_password).hexdigest()

    result = repo.all()
    assert result == [
        User(1, 'david@test.com', '40ccbdf74ca095cbf6a05ede129d3aebdaa16e799b5897be82ca0948fd995d20', 'David', 'dave_test'),
        User(2, 'jane@test.com', '74003ee4634d383f4a1921d434f16e6ef14e2a3259246c130e8a31055250635e', 'Jane', 'jane_test'),
        User(3, 'pickle@test.com', '7052d09741567eaa79757c241d3ee5e2022ad63690ef0f3b2e02f62d5ca6cf6e', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'c6e8b79a09af0a5955447f0fc10348e911a867d11aa4505d411081ace5aa4298', 'John', 'john_test'),
        User(5, 'someone@test.com', hashed_password, 'Someone', 'someone_test')
    ]

def test_update(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    user = repo.find(1)
    user.username = 'happy_face'
    repo.update(user)

    result = repo.all()
    assert result == [
        User(1, 'david@test.com', '40ccbdf74ca095cbf6a05ede129d3aebdaa16e799b5897be82ca0948fd995d20', 'David', 'happy_face'),
        User(2, 'jane@test.com', '74003ee4634d383f4a1921d434f16e6ef14e2a3259246c130e8a31055250635e', 'Jane', 'jane_test'),
        User(3, 'pickle@test.com', '7052d09741567eaa79757c241d3ee5e2022ad63690ef0f3b2e02f62d5ca6cf6e', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'c6e8b79a09af0a5955447f0fc10348e911a867d11aa4505d411081ace5aa4298', 'John', 'john_test')
    ]

def test_delete(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    repo.delete(2)
    result = repo.all()
    assert result == [
        User(1, 'david@test.com', '40ccbdf74ca095cbf6a05ede129d3aebdaa16e799b5897be82ca0948fd995d20', 'David', 'dave_test'),
        User(3, 'pickle@test.com', '7052d09741567eaa79757c241d3ee5e2022ad63690ef0f3b2e02f62d5ca6cf6e', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'c6e8b79a09af0a5955447f0fc10348e911a867d11aa4505d411081ace5aa4298', 'John', 'john_test')
    ]

def test_check_password_for_existing_user(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.check_password('pickle@test.com', 'password333#')
    assert result == True

def test_check_password_for_existing_user_wrong_password(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.check_password('pickle@test.com', 'password444^')
    assert result == False

def test_check_password_for_nonexistent_user(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.check_password('someone@test.com', 'password333!')
    assert result == False

def test_find_by_email(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.find_by_email('david@test.com')
    assert result == User(1, 'david@test.com', '40ccbdf74ca095cbf6a05ede129d3aebdaa16e799b5897be82ca0948fd995d20', 'David', 'dave_test')



