from pessoa import Pessoa
from produto import Produto

class Pedido:

    def __init__(self, end, cliente = None):
        self.id = None
        self.end = end
        self.ciente = cliente
        self.__produtos = []
    
    def addProduto(self, prod):
        if prod is not None:
            self.__produtos.append(prod)
        soma = 0

        for p in self.__produtos:
            soma += p.preco
        return soma
    
    def __str__(self):
        txt = "endereço:" + self.end
        txt += "\n Cliente:" + str(self.cliente)
        txt += "\n Produtos: "
        for p in self.__produtos:
            txt += str(p) + "\n"
        
    def imprimir (self):
        print(self)
        