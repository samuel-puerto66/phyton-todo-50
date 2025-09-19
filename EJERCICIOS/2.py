#samuel puerto 3203084
def promedio(dic):
    edades = [t[0] for t in dic.values()]
    return sum(edades)/len(edades) if edades else 0

if __name__ == "__main__":
    d = {'kevin':(20,'Bogota'), 'david':(15,'Cali')}
    print(promedio(d))
