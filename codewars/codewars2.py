"""
-> Desafio: Stringy Strings
-> Link para o desafio no site: https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python

Instructions:

write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.

"""


def stringy(size):
    string_result = ''

    for i in range(0, size):
        string_result += '1' if i % 2 == 0 else '0'

    return string_result

# TESTANDO:
print(stringy(6))  # out: 101010
print(stringy(9))  # out: 101010101

"""
OUTRA FORMA DE RESOLVER:

def stringy(size):
    return ('10' * size)[:size]

"""
