#samuel puerto 3203084
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2*(self.base + self.altura)

if __name__ == "__main__":
    r = Rectangulo(4,5)
    print("Area:", r.area(), "Perímetro:", r.perimetro())
