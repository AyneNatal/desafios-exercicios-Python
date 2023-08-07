"""
EXERCÍCIO 11) List Comprehension

    A partir das listas aninhadas a seguir:
        nested_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        nested_list2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

    1. Combine-as em uma nova lista usando list comprehension.
"""

nested_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

combined_list = [
    (number, letter) for numbers_list, letters_list in zip(nested_list1, nested_list2)
    for number, letter in zip(numbers_list, letters_list)
]

print(combined_list)  # out: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i')]
