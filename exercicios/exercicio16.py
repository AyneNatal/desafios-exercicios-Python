"""
EXERCÍCIO 16) COMBINAÇÕES

    A partir da lista: people = {'Ana', 'Tom', 'Bia', 'Max'}
        1. Crie uma nova lista com todas as combinações possíveis com os nomes da lista people em grupos de 3 nomes, repetições
        NÃO PODEM acontecer!

        2. Crie uma nova lista com todas as combinões possíveis com os nomes da lista people em grupos de 3 nomes, repetições
        PODEM acontecer.
"""

from itertools import combinations, permutations

people = {'Ana', 'Tom', 'Bia', 'Max'}

# 1)
people_group1 = list(combinations(people, 3))
print(*people_group1, sep='\n')

'''
out:
('Max', 'Bia', 'Ana')
('Max', 'Bia', 'Tom')
('Max', 'Ana', 'Tom')
('Bia', 'Ana', 'Tom')
'''

print('\n ---------------- \n')

# 2)
people_group2 = list(permutations(people, 3))
print(*people_group2, sep='\n')

'''
out:
('Tom', 'Bia', 'Ana')
('Tom', 'Bia', 'Max')
('Tom', 'Ana', 'Bia')
('Tom', 'Ana', 'Max')
('Tom', 'Max', 'Bia')
('Tom', 'Max', 'Ana')
('Bia', 'Tom', 'Ana')
('Bia', 'Tom', 'Max')
('Bia', 'Ana', 'Tom')
('Bia', 'Ana', 'Max')
('Bia', 'Max', 'Tom')
('Bia', 'Max', 'Ana')
('Ana', 'Tom', 'Bia')
('Ana', 'Tom', 'Max')
('Ana', 'Bia', 'Tom')
('Ana', 'Bia', 'Max')
('Ana', 'Max', 'Tom')
('Ana', 'Max', 'Bia')
('Max', 'Tom', 'Bia')
('Max', 'Tom', 'Ana')
('Max', 'Bia', 'Tom')
('Max', 'Bia', 'Ana')
('Max', 'Ana', 'Tom')
('Max', 'Ana', 'Bia')

'''