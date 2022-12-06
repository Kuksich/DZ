x = 0
y = 0
i = 0
while i<2:
    print("Введите направления движенийВ относительно начала координат (0;0), в виде D(Down) - вниз, U(Up) - вверх, R(Right) - вправо, L(Left) - влево. Если хотите остановиться напишите STOP:")
    a = input()
    if a[0] == "U":
        y+=1
        print(x,";",y)
        continue
    if a[0] == "D":
        y-=1
        print(x,";",y)
        continue
    if a[0] == "R":
        x+=1
        print(x,";",y)
        continue
    if a[0] == "L":
        x-=1
        print(x,";",y)
        continue
    if a[0] == "u":
        y+=1
        print(x,";",y)
        continue
    if a[0] == "d":
        y-=1
        print(x,";",y)
        continue
    if a[0] == "r":
        x+=1
        print(x,";",y)
        continue
    if a[0] == "l":
        x-=1
        print(x,";",y)
        continue
    if a =="STOP":
        print("Вы остановились, ваше местоположение: ")
        print(x,";",y)
        break
    if a =="stop":
        print("Вы остановились, ваше местоположение: ")
        print(x,";",y)
        break
        
    
