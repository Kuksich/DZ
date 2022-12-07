from random import randint
list1 = []
list2 = []
i = 0
for i in range(20):
    list1.append(randint(0, 100))
    list2.append(randint(0, 100))
set1 = set(list1)
set2 = set(list2)
print("Первое множество: ", set1)
print("Второе множество: ", set2)
print("Эелементы, входящие в оба множества: ", set1.intersection(set2))
print("Элементы, входящие только в первое множество: ", set1.difference(set2))
print("Элементы, входящие только во второе множество: ", set2.difference(set1))
print("Элементы, входящие в первое и второе, но не в обоих одновременно", set1.symmetric_difference(set2))