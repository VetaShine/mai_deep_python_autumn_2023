"""Декоратор среднего времени исполнения последних parameter вызовов"""
import time
import functools

def mean(parameter):
    """Функция-декоратор"""
    def decorator(func):
        massiv = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            finish = time.time()
            interval = finish - start
            massiv.append(interval)

            if len(massiv) > parameter:
                massiv.pop(0)

            if len(massiv) == parameter:
                average = sum(massiv) / len(massiv)
                print("Среднее время выполнения последних "
                    + str(len(massiv)) + " вызовов: " + str(round(average, 10)) + " секунд")

            return result
        return wrapper
    return decorator

@mean(10)
def call():
    """Функция, которая вызывается декоратором"""

for _ in range(100):
    call()
