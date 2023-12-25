"""
compress: используется для фильтрации элементов из одного набора на основе
другого; в примере продемонстрирована выборка букв алфавита из списка на
основе итерируемого объекта selector:
"""
import itertools

letters = ['А', 'В', 'С', 'D', 'E']
selector = [True, 0, False, 1]

for x in itertools.compress(letters, selector):
    print(x)

# Для объекта selector можно использовать значения
# True/False или 1/0; на выходе будут буквы А и D
