#samuel puerto 3203084
class tupla5:
    def __init__(self, n):
        self.tupla = tuple(x**2 for x in range(1, n+1))

    def a(self):
        print("Tupla", self.tupla)


obj5 = tupla5(6)
obj5.a()
