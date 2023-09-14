"""
EXERCÍCIO 21) Classes & Composição

Crie duas classes, uma chamada Cliente(nome, idade) e outra chamada Endereco(cidade, estado), sendo que:
    1. A classe Cliente deve ter uma função para inserir endereços, onde um Cliente pode ter vários endereços;
    2. A classe Cliente deve ter uma função para listar o cliente e seus endereços.
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # Instancia um objeto Endereco e o adiciona à lista de endereços

    def listar_enderecos(self):
        print(f'Cliente [{self.nome} - {self.idade} anos]:')
        for endereco in self.enderecos:
            print(f'{endereco.cidade} / {endereco.estado}')
        print()


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

# Cliente 1)
cliente1 = Cliente('Max', '67')
cliente1.inserir_enderecos('Dourados', 'MS')
cliente1.inserir_enderecos('Bonito', 'MS')
cliente1.inserir_enderecos('Curitiba', 'PR')

cliente1.listar_enderecos()

# Cliente 2)
cliente2 = Cliente('Poly', 25)
cliente2.inserir_enderecos('Salvador', 'BA')

cliente2.listar_enderecos()

'''
out:
Cliente [Max - 67 anos]:
Dourados / MS
Bonito / MS
Curitiba / PR

Cliente [Poly - 25 anos]:
Salvador / BA
'''