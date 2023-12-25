"""
tee (тройник): используется для дублирования итераторов из единого объекта; ниже приведен
пример дублирования двух итераторов из единого списка:
"""
import itertools

letters = ['А', 'В', 'С']
iter1, iter2 = itertools.tee(letters)

for x in iter1:
    print(x)

for x in iter2:
    print(x)
