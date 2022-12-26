class Human:
    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
    
class Student(Human):
    def __init__(self, name, age, height, weight, gender, plase_of_study, count_of_DZ_done):
        super().__init__(name, age, height, weight, gender)
        self.plase_of_study = plase_of_study
        self.count_of_DZ_done = count_of_DZ_done
        
Dima = Student("Dima", "18", 170, 80, "Male", "YaGK", 8)
Danya = Student("Danya", 17, 180, 60, "Male", "YaGTU", 6)

if Dima.count_of_DZ_done.__gt__(Danya.count_of_DZ_done):
    print("Дима сдал больше ДЗ")
else:
    print("Даня сдал больше ДЗ")