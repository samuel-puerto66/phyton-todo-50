#samuelpuerto 3203084
class Dicc1:
    def __init__(self, n):
        self.dic = {x: x**2 for x in range(1, n+1)}

    def a(self):
        print("Diccionario", self.dic)


obj5 = Dicc1(5)
obj5.a()
