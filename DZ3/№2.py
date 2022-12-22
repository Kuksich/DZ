x = 0
y = 0

while True:
    print("Введите направления движений относительно начала координат, в виде",
          "D(Down) - вниз, U(Up) - вверх, R(Right) - вправо, L(Left) - влево.", 
          "Если хотите остановиться напишите STOP:")
    
    a = input()
    
    if a[0] == "U" or "u":
        y += 1
        print(f"{x}:{y}")
        continue
    
    if a[0] == "D" or "d":
        y -= 1
        print(f"{x}:{y}")
        continue
    
    if a[0] == "R" or "r":
        x += 1
        print(f"{x}:{y}")
        continue
    
    if a[0] == "L" or "l":
        x -= 1
        print(f"{x}:{y}")
        continue
            
    if a =="STOP" or "stop":
        print("Вы остановились, ваше местоположение: ")
        print(f"{x}:{y}")
        break
    
        
    
