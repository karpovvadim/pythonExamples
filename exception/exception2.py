try:
    f = open("аbс.txt", "w")
except Exception as e:
    print("Error:" + e)
else:
    f.write("Hello World\n")
    f.write("End")
finally:
    f.close()
