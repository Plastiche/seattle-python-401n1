from roller import GameLogic

def test_roll_one():

    for _ in range(1000000):
        actual = GameLogic.roll_one()
        assert 1 <= actual <= 6

