"""
EXERCÍCIO 9) Sets

    Dada as listas de linguagens a seguir:
        languages1 = ['python', 'java', 'javascript', 'rust', 'ruby', 'c++', 'python']
        languages2 = ['lua', 'haskell', 'javascript', 'OCaml', 'lua', 'php', 'java', 'ruby']

    1. Crie uma função que retorne um conjunto com todas as linguagens comuns entre as duas listas.
    2. Crie uma função ue retorne um conjunto com todas as linguagens incomuns entre as duas listas.

"""

languages1 = ['python', 'java', 'javascript', 'rust', 'ruby', 'c++', 'python']
languages2 = ['lua', 'haskell', 'javascript', 'OCaml', 'lua', 'php', 'java', 'ruby']

# 1)
def intersection_words(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

print(intersection_words(languages1, languages2))  # {'java', 'javascript', 'ruby'}

# 2)
def difference_words(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.symmetric_difference(set2)

print(difference_words(languages1, languages2))  # {'lua', 'c++', 'rust', 'python', 'OCaml', 'haskell', 'php'}
