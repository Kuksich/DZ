Colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Black", "White", "Brown"]
red = (255, 0, 0)
orange = (255, 165, 0)
white = (255, 255, 255)
black = (0, 0, 0)
brown = (165, 42, 42)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
Dict = {Colours[0]:red, Colours[1]:orange, Colours[2]:yellow, Colours[3]:green, Colours[4]:blue, Colours[5]:black, Colours[6]:white, Colours[7]:brown}
print("Выберите цвет, введите его цифру чтобы узнать его rgb: ")
print("1.Красный 2.Оранжевый 3.Жёлтый 4.Зеленый 5.Синий 6.Черный 7.Белый 8.Коричневый")
a = int(input())
print(Dict.get(Colours[a-1]))