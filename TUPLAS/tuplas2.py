#samuel puerto 3203084
class tupla2:
    def __init__(self):
        self.a = (1, 2, 3)
        self.b = (4, 5, 6)

    def r(self):
        nueva = self.a + self.b
        print("Tupla:", nueva)


obj2 = tupla2()
obj2.r()
