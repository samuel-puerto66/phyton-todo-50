#samuel puerto 3203084
class Agenda:
    def __init__(self):
        self.data = {} 

    def agregar(self, nombre, edad, ciudad):
        self.data[nombre] = (edad, ciudad)

    def obtener(self, nombre):
        return self.data.get(nombre)

if __name__ == "__main__":
    a = Agenda()
    a.agregar('sonia',30,'soacha')
    print(a.obtener('sonia'))
