from random import randint

L = []

#Заполним список 25 случайными элементами
print("Исходный список: ")
for i in range(25):
    L.append(randint(-10, 40))
print(L)

#Сортировка списка методом пузырька
print("Отсортированный список: ")
for i in range(25):
    for j in range(25-i-1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print(L)
            
