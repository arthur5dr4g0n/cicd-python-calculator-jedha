from calculator.calculator import (
    add, subtract, multiply, divide, power, modulo, sqrt, main,
)
import pytest


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_power():
    assert power(2, 10) == 1024


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(1, 0)


def test_sqrt():
    assert sqrt(9) == 3.0


def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)


def test_main_returns_result(capsys):
    assert main(["add", "2", "3"]) == 5.0
    assert "5.0" in capsys.readouterr().out


def test_main_sqrt():
    assert main(["sqrt", "16"]) == 4.0
