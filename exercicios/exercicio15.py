"""
EXERCÍCIO 15) DICTIONARY COMPREHENSION

    1. A partir da string e da lista a seguir, crie um dicionário utilizando dicionary comprehension com as letras da string
    como chaves e os inteiros da lista como valores, a saída deve ser: {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
        letras = 'abcde'
        numeros = [10, 20, 30, 40, 50]

    2. A partir da tupla abaixo, crie um dicionário utilizando dicionary comprehension que possua como chaves os inteiros da tupla
    e como valores uma string informando se o inteiro é um número PAR ou ÍMPAR, a saída deve ser: {1: 'IMPAR', 32: 'PAR', 4: 'PAR', 12: 'PAR', 7: 'IMPAR', 13: 'IMPAR', 29: 'IMPAR', 9: 'IMPAR'}
        inteiros = (1, 32, 4, 12, 7, 13, 29, 9)

"""

# 1.
letras = 'abcde'
numeros = [10, 20, 30, 40, 50]

combinado = {letras[i]: numeros[i] for i in range(0, len(letras))}
print(combinado)  # out: {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# 2.
inteiros = (1, 32, 4, 12, 7, 13, 29, 9)

par_impar = {key: 'PAR' if key % 2 == 0 else 'IMPAR' for key in inteiros}
print(par_impar)  # out: {1: 'IMPAR', 32: 'PAR', 4: 'PAR', 12: 'PAR', 7: 'IMPAR', 13: 'IMPAR', 29: 'IMPAR', 9: 'IMPAR'}
