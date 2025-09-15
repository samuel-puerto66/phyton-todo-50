#samuelpuerto 3203084
class dicc4:
    def __init__(self):
        self.dic = {"a": 20, "b": 40, "c": 60}

    def a(self, clave):
        if clave in self.dic:
            print(f"{clave} -> {self.dic[clave]}")
        else:
            print(f"La clave '{clave}' no existe")


obj2 = dicc4()
obj2.a("b")
obj2.a("z")
