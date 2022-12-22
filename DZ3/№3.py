import math

print("Введите коэффициенты для квадратного уравнения вида ax^2+bx+c=0: ")

a = float(input("a = ")) 
b = float(input("b = ")) 
c = float(input("c = "))

if a == 0:
    x = -c/b
    print("Корень уравнения: ")
    print(f"x = {x}")
    exit()
    
if c == 0:
    x1 = 0
    x2 = -b/a
    print("Корни уравнения:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    if x2 == -b:
        print(f"x3 = {-x2}")
    exit()
    
if b == 0:
    if a > 1:
        c /= a
        a = 1
    if c > 0:
        x = math.sqrt(c)
    if c < 0:
        x = math.sqrt(-c)
    print("Корни уравнения: ")
    print(f"x1 = {x}")
    print(f"x2 = {-x}")
    exit()
    
d = b**2 - 4*a*c

print(f"Дискриминант равен {d}")

if d > 0:
    x1 = ((-b + math.sqrt(d)) / (2*a))
    x2 = ((-b - math.sqrt(d)) / (2*a))
    print("Корни уравнения: ")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    
elif d == 0:
    x = -b/(2*a)
    print("Корень уравнения: ")
    print(f"x = {x}")
    
else:
    print("Корней нет")
    