
try:
    print(x)
    x = 5
    y = 0
    z = x/y
    print('х' + y)

except ZeroDivisionError:
    print("Division bу О is not allowed")
except NameError as e:
    print(e)
except Exception as e:
    print("An error occurred")
    print(e)

