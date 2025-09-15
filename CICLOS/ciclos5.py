#samuel puerto 3203084
class Ciclo5:
    def __init__(self):
        self.nombres = ["Ana", "Luis", "Carlos"]

    def a(self):
        for i, nombre in enumerate(self.nombres, start=1):
            print(f"{i}. {nombre}")


obj5 = Ciclo5()
obj5.a()
