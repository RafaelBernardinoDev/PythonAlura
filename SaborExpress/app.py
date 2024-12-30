from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('praça','gourmet')

def main():
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()