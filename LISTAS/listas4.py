#samuel puerto 3203084
class Suma:
    def __init__(self, lista):
        self.lista = lista

    def suma2(self):
        print("Lista:", self.lista)
        print("Suma:", sum(self.lista))


obj4 = Suma([10, 20, 35, 60])
obj4.suma2()