#samuel puerto 3203084
class Ciclo6:
    def a(self):
        nombres = ["samu", "nico", "kevin"]
        edades = [20, 25, 30]
        for nombre, edad in zip(nombres, edades):
            print(f"{nombre} tiene {edad} años")


obj9 = Ciclo6()
obj9.a()
