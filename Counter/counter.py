"""
Counter (счетчик) - это тип контейнера, который отслеживает количество каждого
элемента, представленного в нем. Он полезен для подсчета частоты встречаемых
данных для последующего анализа.
"""
from collections import Counter

# применение счетчика к объекту строки
print(Counter("people"))

# применение счетчика к объекту списка
my_counter = Counter([1, 2, 1, 2, 3, 4, 1, 3, 1, 1, 3])
print("\nmost_common:", my_counter.most_common(2))  # наиболее общие два элемента
print("elements:", list(my_counter.elements()))

# применение счетчика к объекту словаря
print("\n", Counter({'A': 1, 'В': 2, 'C': 4, 'С': 3}))