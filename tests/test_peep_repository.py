from lib.peep_repository import PeepRepository
from lib.peep import Peep

def test_all(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = PeepRepository(db_connection)

    result = repo.all()
    assert result == [
        Peep(1, 'Hello! This is my very first chitter message!', '2023-05-10 09:05:06', 4),
        Peep(2, 'Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode', '2023-04-22 17:38:19', 1),
        Peep(3, 'I am a cute little kitty cat, and I had a really long nap just now! #toughlife','2023-05-16 14:15:54', 3),
        Peep(4, 'Had a great time at the Makers Academy today! It was fun learning about databases and web apps in Python', '2023-03-08 16:45:30', 2)
    ]

def test_find(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = PeepRepository(db_connection)

    result = repo.find(2)
    assert result == Peep(2, 'Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode', '2023-04-22 17:38:19', 1)

def test_create(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = PeepRepository(db_connection)

    peep = Peep(None, "This is a test message!", "2023-05-22 11:05:34", 4)
    repo.create(peep)
    result = repo.all()
    assert result == [
        Peep(1, 'Hello! This is my very first chitter message!', '2023-05-10 09:05:06', 4),
        Peep(2, 'Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode', '2023-04-22 17:38:19', 1),
        Peep(3, 'I am a cute little kitty cat, and I had a really long nap just now! #toughlife','2023-05-16 14:15:54', 3),
        Peep(4, 'Had a great time at the Makers Academy today! It was fun learning about databases and web apps in Python', '2023-03-08 16:45:30', 2),
        Peep(5, "This is a test message!", "2023-05-22 11:05:34", 4)
    ]

def test_delete(db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    repo = PeepRepository(db_connection)

    repo.delete(4)
    result = repo.all()
    assert result == [
        Peep(1, 'Hello! This is my very first chitter message!', '2023-05-10 09:05:06', 4),
        Peep(2, 'Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode', '2023-04-22 17:38:19', 1),
        Peep(3, 'I am a cute little kitty cat, and I had a really long nap just now! #toughlife','2023-05-16 14:15:54', 3)
    ]
