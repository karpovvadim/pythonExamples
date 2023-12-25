import pytest
from my_pytest.myadd2 import add


def test_add1():
    """Тест для проверки двух положительных чисел"""
    assert add(10, 5) == 15


def test_add2():
    """Тест для проверки двух отрицательных чисел"""
    assert add(-10, -5) == -15, "should bе -15"


def test_add3():
    assert add(10, -5) == 5, "should bе 5"


def test_add4():
    """Тест для проверки двух отрицательных чисел"""
    assert add(-10, 5) == -5, "should bе -5"
