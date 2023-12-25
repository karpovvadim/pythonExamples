"""
Три функции-декоратора
"""
from datetime import datetime


def add_timestamp(func):
    def wrapper(*args, **kwargs):
        res = "{}: {}\n".format(datetime.now(), func(*args, **kwargs))
        return res
    return wrapper


def func_file(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open("log.txt", 'a') as f:
            f.write(res)
            return res
    return wrapper


def console(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res
    return wrapper


@func_file
@add_timestamp
def log(msg):
    return msg


@func_file
@console
@add_timestamp
def log1(msg):
    return msg


@console
@add_timestamp
def log2(msg):
    return msg


log("1) This is а test message for file only")
log1("2) This is а test message for both file and console")
log2("3) This message is for console only")
