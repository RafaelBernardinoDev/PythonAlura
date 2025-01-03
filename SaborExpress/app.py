from modelos.restaurante import Restaurante
# from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Burguer King','Lanche')
#bebida_suco = Bebida('Suco de Laranja', 3,'Pequeno')
prato = Prato('Pão na chapa', 2, 'Pão na chapa com manteiga original')
restaurante_praca.adicionar_prato_no_cardapio(prato)
#restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)

def main():
    print(prato)

if __name__=='__main__':
    main()