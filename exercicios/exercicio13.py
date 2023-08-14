"""
EXERCÍCIO 13) Listas

    Dada as duas listas a seguir:
        lista_a = [1, 2, 3, 4, 5, 6, 7]
        lista_b = [1, 2, 3, 4]

    1. Some os valores nas listas retornando uma nova lista com os valores somados, se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# com loop for padrão:

lista_soma = []

for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)  # out: [2, 4, 6, 8]


# com list comprehension e range():

lista_soma2 = [lista_a[i] + lista_b[i] for i in range(len(lista_b))]
print(lista_soma2)  # out: [2, 4, 6, 8]


# com list comprehension, list() e zip():

lista_soma3 = [sum(list(i)) for i in list(zip(lista_a, lista_b))]
print(lista_soma3)  # out: [2, 4, 6, 8]


# com list comprehension e zip():

lista_soma4 = [num1 + num2 for num1, num2 in zip(lista_a, lista_b)]
print(lista_soma4)  # out: [2, 4, 6, 8]