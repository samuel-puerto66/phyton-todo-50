#samuel puerto 3203084
def a(personas):
    return {nombre: datos for nombre, datos in personas}

if __name__ == "__main__":
    datos = [('kevin',(20,'mosquera')), ('david',(17,'Cali'))]
    print(a(datos))
