"""
chain (цепь): комбинирует два и более итерируемых объекта и возвращает
объединенный объект; ниже приведен пример с двумя итерируемыми объектами
(списками) и функцией chain:
"""
import itertools

list1 = ['А', 'В', 'С']
list2 = ['W', 'X', 'Y', 'Z']
chained_iter = itertools.chain(list1, list2)
# print(list(chained_iter))
for x in chained_iter:
    print(x)

print("\n", list(chained_iter))
