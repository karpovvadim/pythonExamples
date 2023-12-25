def add(x, y):
    """Эта функция складывает 2 числа"""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("only numbers are allowed")
    print("x + y =", x + y)
    return x + y
