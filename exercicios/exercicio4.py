"""
EXERCÍCIO 4) List Comprehension:

    Com relação a List Comprehension:
        1. Crie uma lista com o dobro dos numeros de 1 a 5;
        2. Dada a lista numeros = [1, 3, 4, 5, 6, 7, 8, 9, 10], crie outra lista somente com os numeros pares;
        3. Dada a lista texto = ['Python', 'is', 'Awesome'], crie uma nova lista com as primeiras letras dessa lista;
        4. Dada as listas nums = [1, 2, 3] e letras = ['A', 'B', 'C], combine-as em uma nova lista

"""


# 1)
dobro = [num * 2 for num in range(1, 6)]
print(dobro)  # out: [2, 4, 6, 8, 10]

# 2)
numeros = [1, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]
print(pares)  # out: [4, 6, 8, 10]

# 3)
texto = ['Python', 'is', 'Awesome']

letras_texto = [letra[0] for letra in texto]
print(letras_texto)  # out: ['P', 'i', 'A']

# 4)
nums = [1, 2, 3]
letras = ['A', 'B', 'C']

nums_e_letras = [(num, letra) for num in nums for letra in letras]
print(nums_e_letras)  # out: [(1, 'A'), (1, 'B'), (1, 'C'), (2, 'A'), (2, 'B'), (2, 'C'), (3, 'A'), (3, 'B'), (3, 'C')]
