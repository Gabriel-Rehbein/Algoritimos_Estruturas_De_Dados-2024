from Produto import Produto
from Categoria import Categoria

class Perecivel(Produto):
    def __init__(self, nome, preco = 5.0, cat = Categoria(""), tempMax = 7):
        super().__init__(nome, preco, cat)
        self.temperaturaMaxima = tempMax
    
    def __str__(self):
        return super().__str__() + "\n temperatura Maxima: " + str(self.temperaturaMaxima)
        return txt