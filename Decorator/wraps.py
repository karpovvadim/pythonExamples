"""
Использование wraps предоставит дополнительные сведения о выполнении
вложенных функций
"""

from datetime import datetime
from functools import wraps


def add_timestamps(f):
    @wraps(f)
    def wrapper():
        print(datetime.now())
        f()
        print(datetime.now())
    return wrapper


@add_timestamps
def hello_world():
    """Return a friendly greeting."""
    print("hello world!")


hello_world()
print("A:", hello_world)
print("B:", hello_world.__name__)
print("C:", hello_world.__doc__)
help(hello_world)
