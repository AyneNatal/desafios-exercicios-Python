"""
EXERCÍCIO 6) LOOPS:

    Usando loop while ou for:

        1. A partir da string nome = 'Gertrudes' itere e acrescente um asterísco a cada letra. Ex: 'G*e*r*t*r*u*d*e*s'.
        2. Itere a mesma string e faça com que a saída seja no seguinte formato:
            G
            Ge
            Ger
            Gert... (continua até o nome ficar completo)
"""


nome = 'Gertrudes'

# 1)
nome_asterisco = ''

for i, letra in enumerate(nome):
    if i == len(nome) - 1:  # se for a última letra, ñ coloca o *, somente a letra
        nome_asterisco += letra
    else:
        nome_asterisco += f'{letra}*'

print(nome_asterisco)  # out: G*e*r*t*r*u*d*e*s


# 2)
nome_fragmentado = ''

for letra in nome:
    nome_fragmentado += letra
    print(nome_fragmentado)

# out do segundo for:
# G
# Ge
# Ger
# Gert
# Gertr
# Gertru
# Gertrud
# Gertrude
# Gertrudes




