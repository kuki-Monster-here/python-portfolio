def log_time(func):
    def wrapper(*args):
        print(f"Запуск {func.__name__}...")
        result = func(*args)
        print("Готово!")
        return result
    return wrapper

@log_time
def calculate(a, b):
    return a + b

print(calculate(2, 3))
