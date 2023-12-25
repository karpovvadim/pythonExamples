def power_calc(base):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            exponent = func(*args, **kwargs)
            return base ** exponent
        return wrapper
    return inner_decorator


@power_calc(base=3)  # вычисляем степень значения base, которое передается
def power_n(n):      # декоратору в качестве аргумента.
    return n


print(power_n(2))
print(power_n(4))
