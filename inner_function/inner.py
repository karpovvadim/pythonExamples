"""
Внедрение одной функции в другую
Когда мы добавляем одну функцию внутри другой, она носит название внутренней
или вложенной. Преимущества таких функций заключается в прямом доступе к
переменным, которые определены или доступны в области видимости внешней
функции.
Инкапсуляция
Распространенный вариант использования вложенных функций - возможность
скрыть их функционал от внешнего мира. Они доступны только в пределах области
действия внешней функции и скрыты от области действия глобальной функции.
"""


def outer_hello(who):
    print("Hello from outer function")

    def inner_hello():
        print("Hello from inner function")
        print(f"Hello, {who}")

    inner_hello()


outer_hello("World!")


def factorial(number):
    # Валидация входного значения
    if not isinstance(number, int):
        raise TypeError("Число должно быть целым.")
    if number < 0:
        raise ValueError("Число должно быть неотрицательным.")

    # Расчет факториала
    def inner_factorial(num):
        if num <= 1:
            return 1
        return num * inner_factorial(num - 1)

    return inner_factorial(number)


print("\nfactorial(4) =", factorial(4), "\n")
