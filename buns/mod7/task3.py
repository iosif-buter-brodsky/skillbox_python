"""
Написать декоратор timer. Применить все 3 декоратора к функции fibonacci.
С помощью декоратора timer сравнить скорость выполнения функции fibonacci с декоратором memoize и без него.
"""

import time

def example_decorator(func):
    def wrapper(*args,):
        arg = args[0]
        if len(args) != 1:
            if len(args) > 1:
                return "Too many arguments"
            else:
                return "Not enough arguments"
        
        if not(isinstance(arg, int)):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"
        
        return func(*args)
    return wrapper

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        wrapper.end_time = time.time()
        wrapper.execution_time = wrapper.end_time - start_time
        return result
    return wrapper

@timer
@memoize
@example_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(23)
print(f"Результат fibonacci(10): {result}")
print(f"Функция выполнялась {fibonacci.execution_time:.6f} секунд")
print()

@timer
@example_decorator
def fibonacci_long(n):
    if n < 2:
        return n
    return fibonacci_long(n - 1) + fibonacci_long(n - 2)
result = fibonacci_long(23)
print(f"Результат fibonacci_long(10): {result}")
print(f"Функция выполнялась {fibonacci_long.execution_time:.6f} секунд")



