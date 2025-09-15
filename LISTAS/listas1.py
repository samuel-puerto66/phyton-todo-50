#samuel puerto 3203084
class Lista1:
    def __init__(self, n):
        self.lista = [i**2 for i in range(1, n+1)]

    def mostrar(self):
        print("Lista", self.lista)


obj1 = Lista1(5)
obj1.mostrar()