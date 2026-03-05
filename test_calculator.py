import pytest
import math
from calculator import Calculator


def test_add():
    assert Calculator.add(2, 3) == 5


def test_subtract():
    assert Calculator.subtract(5, 3) == 2


def test_multiply():
    assert Calculator.multiply(4, 3) == 12


def test_divide():
    assert Calculator.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)


def test_power():
    assert Calculator.power(2, 3) == 8


def test_square_root():
    assert Calculator.square_root(9) == 3


def test_square_root_negative():
    with pytest.raises(ValueError):
        Calculator.square_root(-9)


def test_logarithm():
    assert Calculator.logarithm(math.e) == 1


def test_factorial():
    assert Calculator.factorial(5) == 120
