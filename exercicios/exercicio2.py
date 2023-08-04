"""
EXERCÍCIO 2) HIGHER ORDER FUNCTIONS & CLOSURE

    1. Crie uma função que receba outra função cujo intuito seja gerar a tabuada de 5.
"""

def multiplicar_por(num):
    def operador(op):
        return f'{num} * {op} = {num * op}'
    return operador

tabuada_de_5 = multiplicar_por(5)

for i in range(0, 11):  # for p/ iterar os nums de 0 a 10 e multiplicar por 5
    print(tabuada_de_5(i))


"""
output:
5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
"""