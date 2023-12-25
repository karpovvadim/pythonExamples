
with open("my_file.txt", 'w') as f1:
    f1.write("This is а sample file\n")
    lines = ["This is а test data\n", "in two lines\n"]
    f1.writelines(lines)

with open("my_file.txt", 'r') as f2:
    for line in f2.readlines():
        print(line)
