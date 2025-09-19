#samuel puerto 3203084
import random
def adivina(maximo=20):
    secreto = random.randint(1, maximo)
    intentos = 0
    while True:
        intento = int(input(f"Adivina (1-{maximo}): "))
        intentos += 1
        if intento == secreto:
            print("¡Acertaste en", intentos, "intentos!")
            return intentos
        elif intento < secreto:
            print("Mayor")
        else:
            print("Menor")

if __name__ == "__main__":
    print("Función adivina definida.")
