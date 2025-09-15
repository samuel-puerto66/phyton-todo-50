#samuelpuerto 3203084
class dicc3:
    def __init__(self):
        self.dic = {"x": 50, "y": 100}

    def a(self):
        self.dic["z"] = 300
        print("se agrego:", self.dic)
        self.dic.pop("x") 
        print("se elimino:", self.dic)


obj3 = dicc3()
obj3.a()
