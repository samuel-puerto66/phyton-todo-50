#samuelpuerto 3203084
class dic2:
    def __init__(self):
        self.dic = {"Python": 2000, "Java": 2025, "django": 2025}

    def a(self):
        for k, v in self.dic.items():
            print(f"{k} ultima actualizacion {v}")


obj4 = dic2()
obj4.a()
