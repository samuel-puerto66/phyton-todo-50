#samuel puerto 3203084
class PAR:
    def __init__(self, lista):
        self.lista = lista

    def par(self):
        par = [x for x in self.lista if x % 2 == 0]
        print("Lista original:", self.lista)
        print("Solo pares:", par)


obj5 = PAR([1,2,3,4,5,6,7,8,9,10])
obj5.par()