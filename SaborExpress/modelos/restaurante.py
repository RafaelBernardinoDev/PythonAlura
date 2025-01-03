from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cadarpio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo} | {restaurante.media_avaliacao} ')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def alterar_status(self):
        self._ativo = not self._ativo 

    def receber_avaliacao(self,cliente,nota):
        avalicao = Avaliacao(cliente,nota)
        self._avaliacao.append(avalicao)

    @property  
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'Sem Avaliação'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidadeNotas = len(self._avaliacao)
        media = round(soma / quantidadeNotas,2) 
        return media

    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cadarpio.append(item)
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante{self._nome}\n')
        for i,item in enumerate(self._cadarpio,start=1):
            mensagem = f'{i}. Nome:{item._nome} | Preço: {item._preco}'
            print(mensagem)

    


