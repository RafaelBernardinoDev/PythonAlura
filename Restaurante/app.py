from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante = Restaurante('Burguer King','Lanche')
prato = Prato('Pão na chapa', 2.00, 'Pão na chapa com manteiga original')
bebida = Bebida('Suco de Laranja',3.00,'Suco de Laranja Fresco')
restaurante.adicionar_no_cardapio(prato)
restaurante.adicionar_no_cardapio(bebida)

prato.aplicar_desconto()

def main():
    restaurante.exibir_cardapio

if __name__=='__main__':
    main()