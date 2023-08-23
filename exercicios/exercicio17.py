"""
EXERCÍCIO 17) Loop while & listas

    1. Faça uma lista de compras com list();
    2. O usuário deve ter as possibilidades de inserir, apagar, listar os valores e encerrar o programa;
    3. Não permita que o usuário entre com opções inválidas.

    Obs: Desenvolva a lógica do programa usando o Loop While!
"""


lista_de_compras = []

print('\n-- Lista de Compras --')

while True:
    entrada_usuario = input('\n[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: ')

    if entrada_usuario == '1':
        item_inserir = input('Item: ').upper()
        lista_de_compras.append(item_inserir)

    elif entrada_usuario in ['2', '3'] and len(lista_de_compras) == 0:
        print('A lista não possui items')

    elif entrada_usuario == '2':
        item_apagar = input('Item a apagar: ').upper()

        if item_apagar in lista_de_compras:
            lista_de_compras.remove(item_apagar)
            print(f'Item {item_apagar} foi removido\n')
        else:
            print('Item não está na lista')

    elif entrada_usuario == '3':
        for i, item in enumerate(lista_de_compras, 1):
            print(f'{i}- {item}')

    elif entrada_usuario == '4':
        if len(lista_de_compras) == 0:
            print('A lista não possui items')
            break

        print('\nÚltima Lista criada:')
        for i, item in enumerate(lista_de_compras, 1):
            print(f'{i}- {item}')
        break

    else:
        print('Insira uma opção válida')

'''
out (1):

-- Lista de Compras --

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 1
Item: manga

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 1
Item: banana

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 1
Item: arroz

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 3
1- MANGA
2- BANANA
3- ARROZ

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 2
Item a apagar: manga
Item MANGA foi removido


[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 3
1- BANANA
2- ARROZ

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 4

Última Lista criada:
1- BANANA
2- ARROZ


out (2):

-- Lista de Compras --

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 1
Item: farinha

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 2
Item a apagar: arroz
Item não está na lista

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: rty
Insira uma opção válida

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 3
1- FARINHA

[1] Inserir, [2] Apagar, [3] Listar, [4] Encerrar: 4

Última Lista criada:
1- FARINHA

'''