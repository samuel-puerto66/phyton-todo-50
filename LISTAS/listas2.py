#samuel puerto 3203084
class Buscar:
    def __init__(self, lista):
        self.lista = lista

    def Buscar2(self, numero):
        if numero in self.lista:
            print(f"{numero} está en la lista")
        else:
            print(f"{numero} no está en la lista")


obj2 = Buscar([10, 20, 30, 40])
obj2.Buscar2(30)
obj2.Buscar2(50)