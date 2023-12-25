def power(func):
    def wrapper(*args, **kwargs):
        print("Decorating power function")
        n = func(*args, **kwargs)
        return n

    return wrapper


@power
def power_base2(n):
    return 2 ** n


print(power_base2(5))
