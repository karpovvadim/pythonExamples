"""
Лямбда-функции (Lambda function) - это анонимные функции, основанные на
однострочном выражении. В случае с регулярными функциями мы определяем их
ключевым словом def, тогда как анонимные функции определяются словом lambda.
Они ограничены одной строкой, поэтому не могут содержать несколько операторов
и не могут использовать оператор return. Значение возвращается автоматически
после вычисления однострочного выражения.
Лямбда-функции можно использовать везде, где используются обычные функции.
Самый простой и удобный способ - map, reduce и filter. Такие функции помогают
сделать код аккуратным.
"""
mylist = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x * x, mylist))
print(new_list)

# lambda2.py получение четных чисел из списка
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(filter(lambda x: x % 2 == 0, mylist))
print(new_list)

# lambdaЗ.py :вычисление произведения элементов в двух списках
mylist1 = [1, 2, 3, 4, 5]
mylist2 = [6, 7, 8, 9]
new_list = list(map(lambda x, y: x * y, mylist1, mylist2))
print(new_list)