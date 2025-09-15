#samuel puerto 3203084
class Lista3:
    def __init__(self, lista):
        self.lista = lista

    def invertir(self):
        print("normal:", self.lista)
        print("alrevez:", self.lista[::-1])


obj3 = Lista3([100, 20, 35, 40, 500])
obj3.invertir()