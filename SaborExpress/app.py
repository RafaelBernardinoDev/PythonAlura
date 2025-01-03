from modelos.restaurante import Restaurante
# from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Burguer King','Lanche')
prato = Prato('Pão na chapa', 2, 'Pão na chapa com manteiga original')
restaurante_praca.adicionar_no_cardapio(prato)


def main():
    print(prato)

if __name__=='__main__':
    main()