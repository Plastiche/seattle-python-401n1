import pytest
from tests.flow.flo import Flo

pytestmark = [pytest.mark.version_2, pytest.mark.version_3]


def test_quitter():

    Flo.test("tests/flow/quitter.txt")


@pytest.mark.skip("pending")
def test_do_wanna_play_then_quit():

    Flo.test("tests/flow/do_wanna_play_then_quit.txt")


@pytest.mark.skip("pending")
def test_bank_one_roll_then_quit():

    Flo.test("tests/flow/bank_one_roll_then_quit.txt")


@pytest.mark.skip("pending")
def test_bank_first_for_two_rounds():

    Flo.test("tests/flow/bank_first_for_two_rounds.txt")


@pytest.mark.skip("pending")
def test_living_on_the_edge():

    Flo.test("tests/flow/living_on_the_edge.txt")
