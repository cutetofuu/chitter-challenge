from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.all()
    assert result == [
        User(1, 'david@test.com', 'password111', 'David', 'dave_test'),
        User(2, 'jane@test.com', 'password222', 'Jane', 'jane_test'),
        User(3, 'pickle@test.com', 'password333', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'password444', 'John', 'john_test')
    ]

def test_find(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    result = repo.find(3)
    assert result == User(3, 'pickle@test.com', 'password333', 'Pickle', 'pickle_test')

def test_create(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    user = User(None, 'someone@test.com', 'password999', 'Someone', 'someone_test')
    repo.create(user)

    result = repo.all()
    assert result == [
        User(1, 'david@test.com', 'password111', 'David', 'dave_test'),
        User(2, 'jane@test.com', 'password222', 'Jane', 'jane_test'),
        User(3, 'pickle@test.com', 'password333', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'password444', 'John', 'john_test'),
        User(5, 'someone@test.com', 'password999', 'Someone', 'someone_test')
    ]

def test_update(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    user = repo.find(1)
    user.username = 'happy_face'
    repo.update(user)

    result = repo.all()
    assert result == [
        User(1, 'david@test.com', 'password111', 'David', 'happy_face'),
        User(2, 'jane@test.com', 'password222', 'Jane', 'jane_test'),
        User(3, 'pickle@test.com', 'password333', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'password444', 'John', 'john_test')
    ]

def test_delete(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = UserRepository(db_connection)

    repo.delete(2)
    result = repo.all()
    assert result == [
        User(1, 'david@test.com', 'password111', 'David', 'dave_test'),
        User(3, 'pickle@test.com', 'password333', 'Pickle', 'pickle_test'),
        User(4, 'john@test.com', 'password444', 'John', 'john_test')
    ]