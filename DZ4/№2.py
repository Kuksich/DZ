Colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Black", "White", "Brown"]

#RGB набор цветов
red = (255, 0, 0)
orange = (255, 165, 0)
white = (255, 255, 255)
black = (0, 0, 0)
brown = (165, 42, 42)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#Словарь соответствий названия цвета и его RGB
Dict = {Colours[0]:red, Colours[1]:orange, Colours[2]:yellow, Colours[3]:green, Colours[4]:blue, Colours[5]:black, Colours[6]:white, Colours[7]:brown}
print("Выберите цвет, введите его цифру чтобы узнать его rgb:\n",
      "\b1.Красный \n2.Оранжевый \n3.Жёлтый \n4.Зеленый \n5.Синий \n6.Черный \n7.Белый \n8.Коричневый")
try:
    a = int(input())
except ValueError:
    print("Введите число")
    
print(Dict.get(Colours[a-1]))