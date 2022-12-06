x = 0
y = 0
i = 0
print("Введите направления движенийВ относительно начала координат (0;0), в виде D(Down) - вниз, U(Up) - вверх, R(Right) - вправо, L(Left) - влево:")
a = input()
for i in range(len(a)):
    if a[i] == "U":
        y+=1
        continue
    if a[i] == "D":
        y-=1
        continue
    if a[i] == "R":
        x+=1
        continue
    if a[i] == "L":
        x-=1
        continue
    if a[i] == "u":
        y+=1
        continue
    if a[i] == "d":
        y-=1
        continue
    if a[i] == "r":
        x+=1
        continue
    if a[i] == "l":
        x-=1
        continue
print(x,":",y)
