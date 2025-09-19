#samuel puerto 3203084
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        return f"{self.nombre}, {self.edad} años"

if __name__ == "__main__":
    p = Persona('David', 28)
    print(p.info())
