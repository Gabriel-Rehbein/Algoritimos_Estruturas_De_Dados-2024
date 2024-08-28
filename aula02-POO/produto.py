from categoria import Categoria

class Produto:
    def __init__(self, nome, preco = 3 , cat = Categoria ("Tanto Faz")):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.categoria = cat


    def __str__(self):
        txt = "nome:" + self.nome
        txt += "\n preco:" + str(self.preco)
        txt += "\n categoria " + self.categoria.nome
        return txt
        
