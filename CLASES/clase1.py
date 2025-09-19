#samuel puerto 3203084
class Cuenta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad requerida")
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad requerida")
        if cantidad > self.saldo:
            raise ValueError("insuficientes")
        self.saldo -= cantidad

    def __str__(self):
        return f"Cuenta({self.titular}): {self.saldo}"

if __name__ == "__main__":
    c = Cuenta('Samuel', 100.0)
    c.depositar(50)
    try:
        c.retirar(200)
    except Exception as e:
        print("Errorrrrrrrrrrr:", e)
    print(c)
