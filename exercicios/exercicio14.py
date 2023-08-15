"""
EXERCÍCIO 14) DICTIONARY CONPREHENSION

    1. A partir do dict abaixo, crie uma novo dict com o dobro dos valores do dict original, use dictionary comprehension.
        dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    2. Crie um dict usando dictionary comprehension que possua em seus valores o quadrado dos números de 1 a 5, a saída deve ser a seguinte: # out: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""

# 1.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dobro = {key: value * 2 for key, value in dicionario.items()}
print(dobro)  # out: {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

# 2.
quadrado = {value: value ** 2 for value in range(1, 6)}
print(quadrado)  # out: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
