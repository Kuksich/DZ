def summa():
    """Сумма элементов
    
    Принимает:
        Любое количество элементов
    Возвращает:
        Сумму элементов числового типа
    """
    a = input().split()
    s = 0
    for i in a:
        if i.isnumeric():
            s += int(i)
    return s

 
print(summa())