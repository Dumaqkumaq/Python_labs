def log_decorator(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        import time
        start_time = time.time()
        str_out = f"[{(str)(datetime.now().time())}] "
        str_out += f"Функция '{(str)(func.__name__)}' вызвана с аргументами {(str)(args)}\n"

        func(*args)

        str_out += f"[{(str)(datetime.now().time())}] "
        str_out += f"Функция '{(str)(func.__name__)}' завершена. Время выполнения {time.time() - start_time} сек\n"
        with open("log.txt", "a") as fl:
            fl.write(str_out)
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise ValueError("Неподдерживаемая операция")
calculate(10, 5, '/')

#---- 3 -----
def cache_decorator(func):
    mem = {}
    def wrapper(*args):
        if args in mem:
            return  mem[args]
        else:
            rv = func(*args)
            mem[args] = rv
            return rv
    return wrapper

@log_decorator
def fibonacci(n):
    return _fibonacci(n)
def _fibonacci(n):
    if n <= 1:
        return n
    return _fibonacci(n-1) + _fibonacci(n-2)

print(fibonacci(50))
