#samuel puerto 3203084
class Ciclo7:
    def ejecutar(self):
        nombres = ["Ana", "Luis", "Pedro"]
        for i, nombre in enumerate(nombres, start=1):
            print(f"{i}. {nombre}")


obj8 = Ciclo7()
obj8.ejecutar()
