with open("1.txt") as file1, open("2.txt") as file2:
    print(file2.readline())
    print(file1.readline())


with open("1.txt", 'r') as file1, open("3.txt", 'w') as file2:
    for line in file1.readlines():
        file2.write(line)
