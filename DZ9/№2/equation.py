import math

def equat(a, b, c):

    if a == 0:
        x = -c/b
        return x

    if b == 0:
        if a > 0:
            c /= a
            a = 1
        if c > 0:
            x1 = math.sqrt(c)
        if c < 0:
            x1 = math.sqrt(-c)
        x2 = -x1
        return x1, x2
        
    if c == 0:
        x1 = 0
        x2 = -b/a
        if x2 == -b:
            x3 = -b
            return x3
        return x1, x2


    d = b**2 - 4*a*c
    if d > 0:
        x1 = ((-b + math.sqrt(d)) / (2*a))
        x2 = ((-b - math.sqrt(d)) / (2*a))
        return x1, x2

    if d == 0:
        x = -b / (2*a)
        return x

    if d < 0:
        x1 = complex(-b/(2*a), math.sqrt(-d) / (2*a))
        x2 = complex(-b/(2*a), -math.sqrt(-d) / (2*a))
        return x1, x2

