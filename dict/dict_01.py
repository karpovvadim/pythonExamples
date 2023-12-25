# Создание или определение вложенного словаря

dict1 = {100: {'name': 'John', 'age': 24},
         101: {'name': 'Mike', 'age': 22},
         102: {'name': 'Jim', 'age': 21}
         }

print(dict1, "\n")
print(dict1.get(100), "\n")

# Добавление во вложенный словарь
# определение внутреннего словаря 1
student_01 = {'name': 'John', 'age': 24}

# определение внутреннего словаря 2
student_02 = {}
student_02['name'] = 'Mike'
student_02['age'] = '22'

# назначение внутренних словарей 1 и 2 корневому словарю
root_dict = {}
root_dict[100] = student_01
root_dict[101] = student_01

# создание внутреннего словаря напрямую внутри корневого словаря
root_dict[102] = {}
root_dict[102]['name'] = 'Jim'
root_dict[102]['age'] = '21'

print("root_dict", root_dict, "\n")
print(root_dict.get(102))

