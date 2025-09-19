def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    cuenta = 0
    for ch in cadena:
        if ch in vocales:
            cuenta += 1
    return cuenta

if __name__ == "__main__":
    print(contar_vocales('Hola Mundo'))
