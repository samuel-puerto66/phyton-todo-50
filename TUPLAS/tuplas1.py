#samuel puerto 3203084
class tupla1:
    def __init__(self):
        self.tupla = ("python", "java", "c++", "django")

    def ver(self):
        print("Primero:", self.tupla[0])
        print("Último:", self.tupla[-1])


obj1 = tupla1()
obj1.ver()