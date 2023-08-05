"""
EXERCÍCIO 7) List Comprehension

    Dada a Lista: numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        1. Crie uma nova lista utilizando list comprehension com os números primos presentes na lista original.

"""
import math

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_primos = [num for num in numeros if all(num % i != 0 for i in range(2, math.isqrt(num) + 1)) and num != 1]
print(num_primos)  # out: [2, 3, 5, 7]
