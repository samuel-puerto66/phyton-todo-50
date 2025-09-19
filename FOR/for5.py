class ContadorFor:
    def __init__(self, iterable):
        self.iterable = iterable

    def contar(self, funcion_condicion):
        contador = 0
        for x in self.iterable:
            if funcion_condicion(x):
                contador += 1
        return contador

if __name__ == "__main__":
    c = ContadorFor(range(1,21))
    print("Pares en 1..20:", c.contar(lambda x: x%2==0))
