def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


try:
    n = int(input())
    if n <= 0:
        raise ValueError
except ValueError:
    print("Value Error")
    exit()

print(fib(n))