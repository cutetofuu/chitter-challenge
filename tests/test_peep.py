from lib.peep import Peep

def test_constructs():
    peep = Peep(1, "This is a test message", "2023-05-08 16:08:34", 4)
    assert peep.id == 1
    assert peep.message == "This is a test message"
    assert peep.created_at == "2023-05-08 16:08:34"
    assert peep.user_id == 4

def test_formatting():
    peep = Peep(1, "This is a test message", "2023-05-08 16:08:34", 4)
    assert str(peep) == 'Peep(1, This is a test message, 2023-05-08 16:08:34, 4)'

def test_equality():
    peep_1 = Peep(1, "This is a test message", "2023-05-08 16:08:34", 4)
    peep_2 = Peep(1, "This is a test message", "2023-05-08 16:08:34", 4)
    assert peep_1 == peep_2