dict1 = {'а': 100, 'Ь': 200, 'с': 300}
dict2 = {x: int(y/2) for (x, y) in dict1.items() if y <= 200}
print(dict2)
