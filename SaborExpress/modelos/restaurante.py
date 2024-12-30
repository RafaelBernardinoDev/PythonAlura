class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    def StatusAlt(self):
        self._ativo = not self._ativo    



