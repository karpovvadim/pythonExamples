"""
groupby: определяет ключи для каждого элемента в объекте и группирует их на
основе этих ключей; для работы функции требуется другая функция (key_func),
которая идентифицирует ключ в каждом элементе итерируемого объекта; следующий
пример демонстрирует использование обеих функций:
"""

import itertools

mylist = [("А", 100), ("А", 200), ("В", 30), ("В", 10), ("C", 20)]


def get_key(group):
    return group[0]


for key, grp in itertools.groupby(mylist, get_key):
    print(key + "-->", list(grp))