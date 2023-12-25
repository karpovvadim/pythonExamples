"""
reduce (уменьшать)
Функция reduce используется для применения кумулятивной обработки (Cumulative
Processing) к каждому элементу последовательности, которая передается ей в
качестве аргумента. Функция кумулятивной обработки не предназначена для
преобразования или фильтрации. Как следует из названия, она нужна для получения в
конце единого результата на основе всех элементов последовательности. Синтаксис
функции следующий:
reduce (func, iter[, initial])
Функция func используется для применения кумулятивной обработки к каждому
элементу итерируемого объекта. Кроме того, initial - это опциональное значение,
которое можно передать в func в качестве начального значения для обработки.
Важно понимать, что в func всегда нужно будет передавать два аргумента в случае
использования reduce: первым аргументом будет начальное значение (если оно
указано) или первый элемент последовательности, а вторым аргументом будет
следующий элемент последовательности.
"""
from functools import reduce


def seq_sum(num1, num2):
    return num1 + num2


mylist = [1, 2, 3, 4, 5]
result1 = reduce(seq_sum, mylist)
print(result1)  # 15
result = reduce(seq_sum, mylist, 10)
print(result)  # 25
