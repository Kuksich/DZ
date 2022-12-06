d = int(input())
res = ''

while d > 0:
    res = str(d % 2) + res
    d //= 2

print(res)