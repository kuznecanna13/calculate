import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4
    assert calculate(1, 0, '/') == "Ошибка: Деление на ноль."

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_minus():
    assert calculate(3, 2, '-') == 1

def test_calculate_multiply():
    assert calculate(2, 5, '*') == 10
    assert calculate(0, 5, '*') == 0
    assert calculate(0.2, 5, '*') == 1

'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
