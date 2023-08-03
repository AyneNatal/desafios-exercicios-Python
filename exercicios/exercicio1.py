"""
EXERCÍCIO 1)

    -> Dada a lista de dicionários:

    users_list = [
        {'name': 'Tony', 'age': 23},
        {'name': 'Abil', 'age': 31},
        {'name': 'Bia', 'age': 56},
        {'name': 'Lari', 'age': 17},
        {'name': 'Max', 'age': 15},
    ]

    1. Crie uma nova lista com os nomes ordenados em ordem natural.
    2. Crie uma nova lista com os nomes ordenados em ordem inversa.
"""

# RESOLVENDO:

users_list = [
    {'name': 'Tony', 'age': 23},
    {'name': 'Abil', 'age': 31},
    {'name': 'Bia', 'age': 56},
    {'name': 'Lari', 'age': 17},
    {'name': 'Max', 'age': 15},
]

# ordem natural:
nova_lista_ordem_natural = sorted(users_list, key=lambda user: user['name'])
print(*nova_lista_ordem_natural, sep='\n')  # imprimir com um dict em baixo do outro

print()  # saltar uma linha

# ordem inversa:
nova_lista_ordem_inversa = sorted(users_list, key=lambda user: user['name'], reverse=True)
print(*nova_lista_ordem_inversa, sep='\n')

