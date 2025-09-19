#samuel puerto 3203084
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

    def perimetro(self):
        return 2 * math.pi * self.radio

if __name__ == "__main__":
    c = Circulo(3)
    print("Area:", c.area(), "Perímetro:", c.perimetro())
