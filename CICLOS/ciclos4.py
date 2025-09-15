#samuel puerto 3203084
class Ciclo4:
    def a(self):
        x = 0
        while True:
            x += 1
            print("Número", x)
            if x == 3:
                print("Se detuvo")
                break


obj4 = Ciclo4()
obj4.a()
