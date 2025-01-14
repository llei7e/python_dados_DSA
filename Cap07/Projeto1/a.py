class Func:
    def __init__(self, nome):
        self.nome = nome
    
    def listFunc(self):
        print(self.nome)

func1 = Func("Charles")

func1.listFunc()

setattr(func1, "nome", "Lucas")

func1.listFunc()