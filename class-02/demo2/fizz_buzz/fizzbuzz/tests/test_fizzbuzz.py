from fizzbuzz import __version__
from fizzbuzz.fizz_buzz import fizz_buzz


def test_version():
    assert __version__ == '0.1.0'


def test_fizz_buzz_pass():
    actual = fizz_buzz(15)
    expected = 'FizzBuzz'
    assert actual == expected


def test_fizz_buzz_fail():
    actual = fizz_buzz(15)
    expected = 'FizzBuz'
    assert actual != expected


def test_fizz_pass():
    actual = fizz_buzz(3)
    expected = 'Fizz'
    assert actual == expected


def test_fizz_fail():
    actual = fizz_buzz(4)
    expected = "Fizz"
    assert actual != expected


def test_buzz_pass():
    actual = fizz_buzz(5)
    expected = "Buzz"
    assert actual == expected


def test_buzz_fail():
    actual = fizz_buzz(7)
    expected = 'Buzz'
    assert actual != expected


def test_num_pass():
    actual = fizz_buzz(2)
    expected = 2
    assert actual == expected


def test_num_fail():
    actual = fizz_buzz(2)
    expected = 1
    assert actual != expected
