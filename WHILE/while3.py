def suma():
    total = 0
    while True:
        n = float(input("Número (0 para terminar): "))
        if n == 0:
            break
        total += n
    return total

if __name__ == "__main__":
    # Para evitar input en ejecuciones automáticas, mostramos la función
    print("suma definida.")
