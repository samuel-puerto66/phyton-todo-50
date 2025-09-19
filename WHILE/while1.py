def buscar(lista, valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            return i
        i += 1
    return -1

if __name__ == "__main__":
    print(buscar([5,3,7,1], 7))
    print(buscar([5,3,7,1], 2))
