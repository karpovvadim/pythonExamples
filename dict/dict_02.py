# Доступ к элементам вложенного словаря

dict1 = {100: {'name': 'John', 'age': 24},
         101: {'name': 'Mike', 'age': 22},
         102: {'name': 'Jim', 'age': 21}
         }
print(dict1.get(100))
print(dict1.get(100).get('name'))
print(dict1[101])
print(dict1[101]['age'], "\n")

print('Удаление из вложенного словаря')

del (dict1[101]['age'])
print(dict1)
age_Jim = dict1[102].pop('age')
print(dict1)
print("age_Jim:", age_Jim)
