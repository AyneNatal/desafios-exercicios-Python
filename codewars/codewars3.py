"""
-> Desafio: Find Multiples of a Number (8 Kyu)
-> Link para o desafio no site: https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python

Instructions:

In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples up to another value, limit.
If limit is a multiple of integer, it should be included as well.
There will only ever be positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.

For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.

"""


def find_multiples(integer, limit):
    result = []

    for num in range(integer, limit + 1, integer):
        result.append(num)

    return result


print(find_multiples(2, 6))  # out: [2, 4, 6]
print(find_multiples(5, 25))  # out: [5, 10, 15, 20, 25]


"""

OUTRA FORMA DE RESOLVER:

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
    
"""