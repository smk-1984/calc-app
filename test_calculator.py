import pytest
from calculator import add, subtract, multiply, divide, percentage, power, modulo


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_percentage():
    assert percentage(25, 50) == 50.0


def test_power():
    assert power(2, 3) == 8


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(10, 0)


def test_modulo_negative_numbers():
    # Python's % follows the sign of the divisor, e.g. -7 % 3 == 2 (not -1)
    assert modulo(-7, 3) == 2
    assert modulo(7, -3) == -2