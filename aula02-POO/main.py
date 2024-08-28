from produto import Produto
from pessoa import Pessoa
from cidade import Cidade
from categoria import Categoria
from produto import Produto
from pedido import Pedido

cid01 = Cidade()
cid02 = Cidade("Porto Alegre")

p1 = Pessoa ("Joao")
p2 = Pessoa ("Maria, 1.80")
p3 = Pessoa ("José", 1.80, cid01)
p4 = Pessoa ("Julia", cid = cid02)

cat01 = Categoria()


#incompleto, completar!

print (p)