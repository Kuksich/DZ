from random import randint

list1 = []
list2 = []

#Заполним два списка 20 случайными элементами
for i in range(20):
    list1.append(randint(0, 100))
    list2.append(randint(0, 100))

#Преобразуем списки в множества   
set1 = set(list1)
set2 = set(list2)

print(f"Первое множество: {set1}\n",
      f"\bВторое множество: {set2}\n",
      f"\bЭелементы, входящие в оба множества: {set1.intersection(set2)}\n",
      f"\bЭлементы, входящие только в первое множество: {set1.difference(set2)}\n",
      f"\bЭлементы, входящие только во второе множество: {set2.difference(set1)}\n",
      f"\bЭлементы, входящие в первое и второе, но не в обоих одновременно {set1.symmetric_difference(set2)}")