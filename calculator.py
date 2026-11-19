# calculator.py
"""Простой модуль калькулятора для демонстрации unit-тестов."""

import math


def add(a, b):
    """
    Возвращает сумму двух чисел.

    Пример вызова:
        >>> add(2, 3)
        5
    """
    return a + b


def subtract(a, b):
    """
    Возвращает разность двух чисел.

    Пример вызова:
        >>> subtract(10, 4)
        6
    """
    return a - b


def multiply(a, b):
    """
    Возвращает произведение двух чисел.

    Пример вызова:
        >>> multiply(3, 4)
        12
    """
    return a * b


def divide(a, b):
    """
    Возвращает частное. Бросает ValueError при b == 0.

    Пример вызова:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def power(a, b):
    """
    Возвращает a в степени b.

    Пример вызова:
        >>> power(2, 3)
        8
    """
    return a ** b


def sqrt(a):
    """
    Возвращает квадратный корень. Бросает ValueError при a < 0.

    Пример вызова:
        >>> sqrt(9)
        3.0
    """
    if a < 0:
        raise ValueError("Корень из отрицательного числа не определён")
    return math.sqrt(a)
