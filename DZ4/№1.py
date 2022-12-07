from random import randint
i = 0 
j = 0
L = []
print("Исходный список: ")
for i in range(25):
    L.append(randint(-10, 40))
print(L)
print("Отсортированный список: ")
for i in range(25):
    for j in range(25-i-1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print(L)
            
