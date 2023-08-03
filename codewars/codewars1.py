"""
-> Desafio: Removing Elements (8 Kyu)
-> Link para o desafio no site: https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

Instructions:
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""

# Listas para usar no teste da função:
aleatory_list1 = ["Keep", "Remove", "Keep", "Remove", "Keep"]
aleatory_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

# Resolvendo:
def remove_every_other(my_list):
    return my_list[::2]

# Testando:
print(remove_every_other(aleatory_list1))  # out: ['Keep', 'Keep', 'Keep']
print(remove_every_other(aleatory_list2))  # out: [1, 3, 5, 7]
