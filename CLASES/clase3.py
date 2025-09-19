#samuel puerto 3203084
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def nota(self, n):
        self.notas.append(n)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas)/len(self.notas)

if __name__ == "__main__":
    e = Estudiante('samuel puerto')
    e.nota(5)
    e.nota(4)
    print("NOTA DE:", e.promedio())
