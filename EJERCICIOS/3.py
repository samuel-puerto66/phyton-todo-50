#samuel puerto 3203084
def ordenar(dic):
    return dict(sorted(dic.items(), key=lambda kv: kv[1][0]))

if __name__ == "__main__":
    d = {'jona':(60,'B'), 'nico':(35,'C'), 'daniel':(78,'A')}
    print(ordenar(d))
