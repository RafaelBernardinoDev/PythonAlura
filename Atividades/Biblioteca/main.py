from modelos.livro import Livro

livro1 = Livro('Senhor dos Aneis volume 1', 'J. R. R. Tolkien', 1, 1954)
livro1.emprestar()
livro1.disponivel

def main():
    Livro.listar_livro()

if __name__ == '__main__':
    main()
