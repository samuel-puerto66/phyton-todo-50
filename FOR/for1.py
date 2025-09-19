def tabla_multiplicar(n, hasta=10):
    return [n*i for i in range(1, hasta+1)]

if __name__ == "__main__":
    print(tabla_multiplicar(7))
