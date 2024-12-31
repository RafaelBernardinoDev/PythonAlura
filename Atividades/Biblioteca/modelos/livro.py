class Livro:
    _livros = []

    def __init__(self, titulo, autor, quantidade, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._quantidade = quantidade
        self._disponivel = quantidade > 0
        Livro._livros.append(self)

    def __str__(self):
        return f"Livro: {self._titulo}, Autor: {self._autor}, Ano: {self._ano}, Quantidade: {self._quantidade}"

    @classmethod
    def listar_livro(cls):
        for livro in cls._livros:
            print(f'Nome da obra: {livro._titulo}\nAutor: {livro._autor}\nAno de Lançamento: {livro._ano}\nDisponibilidade: {livro.disponivel}\n')

    @property
    def disponivel(self):
        return 'Disponível' if self._quantidade > 0 else 'Indisponível'

    def emprestar(self):
        self._quantidade -= 1
        print('Livro emprestado com sucesso!')






Livro.listar_livro()
