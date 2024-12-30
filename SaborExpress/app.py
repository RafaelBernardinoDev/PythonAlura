from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Burguer King','Lanche')
restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('Rafael',9)
restaurante_praca.alterar_status()


def main():
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()