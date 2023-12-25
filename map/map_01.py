"""
map
Функция map определяется с помощью следующего синтаксиса:
map(func, iter, ...)
Аргумент func - это имя функции, которая будет применяться к каждому элементу
объекта iter. Три точки указывают, что можно передать несколько, итерируемых
объектов. Однако важно понимать, что количество аргументов функции (func)
должно совпадать с числом итерируемых объектов. Результатом функции map будет
объект map (или mар-объект), который является генератором. Возвращаемое значение
можно преобразовать в список, передав объект map конструктору list.
"""
mylist = [1, 2, 3, 4, 5]
new_list = []

for item in mylist:
    square = item * item
    new_list.append(square)
print("без map:", new_list)


def square(num):
    return num * num


mylist = [1, 2, 3, 4, 5]
map_obj = map(square, mylist)
print("\nmap_obj:", map_obj)
new_list = list(map(square, mylist))
print("list(map(square, mylist)):", new_list)


def product(num1, num2):
    return num1 * num2


mylist1 = [1, 2, 3, 4, 5]
mylist2 = [6, 7, 8, 9]
new_list = list(map(product, mylist1, mylist2))
print("\nlist(map(product, mylist1, mylist2)):", new_list)
