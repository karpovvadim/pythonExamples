"""
accumulate: возвращает итератор, который предоставляет общую сумму или другие
накопленные результаты на основе функции-агрегатора, которая была передана в
accumulate в качестве аргумента; легче понять ее работу на примере:
"""
import itertools, operator

list1 = (1, 3, 5)
res = itertools.accumulate(list1)  # по умолчанию accumulate выполнит сложение
print("default:")
for x in res:
    print(x)

res = itertools.accumulate(list1, operator.mul)
print("\nMultiply:")
for x in res:
    print(x)

res = itertools.accumulate(list1, operator.truediv)
print("\nистинный делитель:")
for x in res:
    print(x)