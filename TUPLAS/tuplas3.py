#samuel puerto 3203084
class tupla3:
    def __init__(self):
        self.tupla = (1, 2, 2, 3, 4, 2, 5)

    def c(self, n):
        print(f"El número {n} aparece {self.tupla.count(n)}veces")


obj3 = tupla3()
obj3.c(2)
