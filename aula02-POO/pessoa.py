from cidade import Cidade

class Pessoa:

    def __init__(self, nome, altura = 1.73, cid = Cidade("Itati")):
        self.id = None
        self.nome = nome
        self.altura = altura
        self.cidade = cid

    def __str__(self):
        txt = "nome:" + self.nome
        txt += "\n Altura:" + str(self.altura)
        txt += "\n Cidade " + self.cidade.nome
        return txt
        