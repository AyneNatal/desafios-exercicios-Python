"""
EXERCÍCIO 10) List Comprehension

    A partir da lista aninhada a seguir:
        nested_words = [['apple', 'banana'], ['grape', 'orange'], ['cherry', 'kiwi']]

    1. Usando list comprehension crie uma nova lista com todos os itens em caixa-alta.
    2. Usando list comprehension crie uma nova lista com a primeira letra de cada item em caixa-alta.
"""

nested_words = [['apple', 'banana'], ['grape', 'orange'], ['cherry', 'kiwi']]

# 1)
upper_word_list = [word.upper() for words in nested_words for word in words]
print(upper_word_list)  # out: ['APPLE', 'BANANA', 'GRAPE', 'ORANGE', 'CHERRY', 'KIWI']

# 2)
title_word_list = [letter.title() for word in nested_words for letter in word]
print(title_word_list)  # out: ['Apple', 'Banana', 'Grape', 'Orange', 'Cherry', 'Kiwi']
