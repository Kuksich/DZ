import os
from datetime import datetime
import time
os.chdir("D:\DZ_py\DZ8\№4")    #Сменил директорию работы, чтобы файл с логами открывался

def logs_decorator(func):
    """Декоратор логирования
    
    Логирует функцию разности квадратов и заносит логи в файл logs.txt
    """
    def wrapper(a, b):
        start_time = datetime.now()
        f = open("logs.txt", "w")
        f.write("Function started")
        try:
            func(a, b)
        except TypeError:
            f.write("\nFunction ended because of TypeError")
            f.close
            exit()
        f.write(f"\nFunction received {a} and {b}")
        f.write(f"\nFunction ended, result is {func(a, b)}")
        time.sleep(0.000001)    #Добавил эту стороку, потому что иначе в логах время работы программы было равно нулю
        end_time = datetime.now()
        f.write("\nWorktime of function is {}".format((end_time - start_time)))
        f.close
    return wrapper

@logs_decorator
def random_func(a, b):
    """Разность квадратов
    
    Принимает:
        a - первый аргумент
        b - второй аргумент
    Возвращает:
        Разность квадратов суммы и разности a и b
        ((a+b)**2)-((a-b)**2)
    """
    rez = ((a+b)**2)-((a-b)**2)
    return rez

random_func(51231235235235, 123123)
