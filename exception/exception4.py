"""
В Python можно определить собственное исключение с помощью создания нового
класса, производного от встроенного класса Exception или его подкласса. Для
демонстрации изменим предыдущий пример и определим два пользовательских класса
исключений, заменив ими встроенные типы ошибок TypeError и Exception. Новые
пользовательские классы исключений будут производными от TypeError и Exception.
Пример кода с пользовательскими исключениями:
"""
import math


class NumTypeError(TypeError):
    pass


class NegativeNumError(Exception):
    def __init__(self):
        super().__init__("Negative number not supported")


def sqrt(num):
    if not isinstance(num, (int, float)):
        raise NumTypeError("only numbers are allowed")
    if num < 0:
        raise NegativeNumError
    return math.sqrt(num)


if __name__ == "__main__":
    try:
        print(sqrt(9))
        print(sqrt('а'))
        print(sqrt(-9))
    except NumTypeError as e:
        print("NumTypeError:", e)
    except NegativeNumError as e:
        print("NegativeNumError:", e)
"""
В этом примере класс NumTypeError является производным от класса TypeError, и мы
ничего в него не добавляем. Класс NegativeNumError наследуется от класса Exception,
мы переопределяем его конструктор, добавляя пользовательское сообщение для
этого исключения как часть конструктора. Когда мы вызываем эти пользовательские 
исключения в функции sqrt(), мы не передаем никакого текста с классом исключений
NegativeNumError. Когда мы выполняем основную программу, получаем сообщение с 
оператором print(е), поскольку он задан как часть определения класса. В этом 
подразделе мы рассмотрели, как обрабатывать встроенные типы ошибок с помощью 
блоков try и except, как определять пользовательские исключения и вызывать их 
декларативно.
"""