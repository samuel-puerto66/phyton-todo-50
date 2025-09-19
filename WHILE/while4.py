#samuel puerto 3203084
import random
class ContadorWhile:
    def __init__(self, maximo=10):
        self.secreto = random.randint(1, maximo)
        self.intentos = 0

    def intentar(self, valor):
        self.intentos += 1
        return valor == self.secreto

if __name__ == "__main__":
    cw = ContadorWhile(20)
    for prueba in [5,10,15, cw.secreto]:
        correcto = cw.intentar(prueba)
        print("Probando", prueba, "->", "Correcto" if correcto else "No")
    print("Intentos totales:", cw.intentos)
