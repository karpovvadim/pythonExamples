def is_even(num):
    return num % 2 == 0


mylist = [1, 2, 3, 4, 5, 6, 7]
new_list = list(map(is_even, mylist))
print(new_list)  # [False, True, False, True, False, True, False]
