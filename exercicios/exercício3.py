"""
EXERCÍCIO 3) LOOPS

A partir do texto abaixo:
texto = 'Ragnarok é um MMORPG que se passa em um mundo de fantasia, repleto de aventuras, batalhas épicas e criaturas míticas. Com sua jogabilidade envolvente e comunidade vibrante, Ragnarok conquistou milhões de jogadores em todo o mundo.'

    1. Utilizando os loops WHILE ou FOR, imprima qual letra aparece mais vezes e quantas vezes ela aparece.
"""


texto = 'Ragnarok é um MMORPG que se passa em um mundo de fantasia, repleto de aventuras, batalhas épicas e criaturas míticas. Com sua jogabilidade envolvente e comunidade vibrante, Ragnarok conquistou milhões de jogadores em todo o mundo.'

# FOR:
letra_mais_frequente = ''
contador_letra = 0
alfabeto_pt_br = 'AÁÀÂÃBCÇDEÉÈÊFGHIÍÌÎJKLMNOÓÒÔÕPQRSTUÚÙÛVWXYZ'  # p/ não pegar virgulas, espaços etc.

for letra in texto:
    letra_atual = letra.upper()  # deixando td em caixa alta pra verificação ser 100%
    contador = texto.upper().count(letra_atual)

    if letra_atual in alfabeto_pt_br and contador > contador_letra:
        letra_mais_frequente = letra_atual
        contador_letra = contador

print(f'A letra "{letra_mais_frequente}" é a mais frequente e aparece {contador_letra}x.')


"""
output:
A letra "A" é a mais frequente e aparece 24x.
"""