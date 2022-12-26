class animal:
    def __init__(self, name, age, weight, type_of_food_eating, habitat):
        self.name = name
        self.age = age
        self.weight = weight
        self.type_of_food_eating = type_of_food_eating
        self.habitat = habitat    #среда обитания
        
class mammals(animal):
    def __init__(self, name, age, weight, type_of_food_eating, habitat, lifestyle):
        super().__init__(name, age, weight, type_of_food_eating, habitat)
        self.lifestyle = lifestyle    #Образ жизни(Наземное, водное, древесное, подземное, летающее)

class human(mammals):
    def __init__(self, name, age, weight, type_of_food_eating, habitat,  lifestyle, company, position, income, gender, race, height):
        super().__init__(name, age, weight, type_of_food_eating, habitat, lifestyle)
        self.company = company
        self.position = position
        self.income = income
        self.gender = gender
        self.race = race    #раса
        self.height = height 
        
class cat(mammals):
    def __init__(self, name, age, weight, type_of_food_eating, habitat, lifestyle, color, gender, breed, active):
        super().__init__(name, age, weight, type_of_food_eating, habitat, lifestyle)
        self.color = color
        self.gender = gender
        self.breed = breed    #порода
        self.active = active    #активность животного
        
class dog(mammals):
    def __init__(self, name, age, weight, type_of_food_eating, habitat, lifestyle, color, gender, breed, active):
        super().__init__(name, age, weight, type_of_food_eating, habitat, lifestyle)
        self.color = color
        self.gender = gender
        self.breed = breed    #порода
        self.active = active    #активность животного
        

Dima = human("Dima", "18", 80, "Everything", "Everywhere", "Ground", "YAGK", "Student", "1000", "Male", "Europeoid", "180")
Mussya = cat("Mussya", 4, 5, "Meat", "House", "Ground", "Black", "Female", "American Bobtail", "-")
Bonya = dog("Bonya", 8, 10, "Meat", "Ground", "House", "Female", "Black and White", "Landseer", "+")
print(Bonya.active)
print(Dima.age)
print(Mussya.breed)
