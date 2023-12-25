list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [x + 1 for x in list1]
print(list2)

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list4 = [x for x in list3 if x % 2 == 0]
print(list4)
