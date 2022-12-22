import math
try:
    r = int(input())
except ValueError:
    print("Введите число")
print (math.pi * r**2)