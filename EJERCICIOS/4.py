#samuel puerto 3203084
def actualizar(dic, nombre, nueva):
    if nombre in dic:
        edad = dic[nombre][0]
        dic[nombre] = (edad, nueva)
        return True
    return False

if __name__ == "__main__":
    d = {'Ana':(30,'B')}
    print(actualizar(d,'larita','suame'), d)
