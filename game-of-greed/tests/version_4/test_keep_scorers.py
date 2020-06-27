import pytest
from game_of_greed.game import Game

pytestmark = [pytest.mark.version_4]


@pytest.mark.skip("pending")
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((1, 1, 1, 2, 3, 4), (1, 1, 1)),
        ((1, 1, 5, 2, 3, 5), (1, 1, 5, 5)),
        ((1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 3, 4)),
        ((1, 6, 5, 2, 3), (1, 5)),
    ],
)
def test_keep_scorers(test_input, expected):
    game = Game()
    actual = game.keep_scorers(test_input)
    assert actual == expected
