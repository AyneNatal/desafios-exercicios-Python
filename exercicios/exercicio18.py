"""
EXERCÍCIO 18) Listas, Leitura e Gravação de arquivos

    Você deve construir um programa que crie uma lista de tarefas, onde o usuário poderá inserir uma uma tarefa ou um comando,
    os comandos são Listar, Refazer, Desfazer e Sair que servirão para editar a lista.
    Atenção: Quando o usuário digitar a opção "Sair" a lista deverá ser salva num arquivo.txt em algum lugar no seu PC e o programa
    encerrado.

"""

print('_________  Bem Vindo!  _________\n')
print('Digite suas tarefas ou utilize os comandos:')
print('Listar / Desfazer / Refazer / Sair\n')

lista_tarefas = []
lista_desfazer = []

while True:
    entrada_usuario = input('➡️ Digite uma tarefa ou um comando: ').upper()

    try:
        if entrada_usuario in ['LISTAR', 'DESFAZER', 'REFAZER'] and lista_tarefas == []:
            print('A Lista está Vazia\n')

        elif entrada_usuario == 'LISTAR':
            for i, tarefa in enumerate(lista_tarefas, 1):
                print(f'{i} -- {tarefa}')
            print()

        elif entrada_usuario == 'DESFAZER':
            tarefa_desfeita = lista_tarefas.pop()
            lista_desfazer.append(tarefa_desfeita)

        elif entrada_usuario == 'REFAZER':
            tarefa_refeita = lista_desfazer.pop()
            lista_tarefas.append(tarefa_refeita)

        elif entrada_usuario == 'SAIR':
            print('-- Lista de Tarefas Salva - Programa Encerrado --')
            with open('C:\\Users\\digiteSeuUserAqui\\Downloads\\lista_de_tarefas.txt', 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write('\n'.join(['🔹' + tarefa for tarefa in lista_tarefas]))
            break

        else:
            lista_tarefas.append(entrada_usuario)
    except IndexError as error:
        print('Não existem mais tarefas a serem restauradas')


'''
Disclaimer:
A lista de tarefas foi salva na pasta Download do Windows11, se você quiser usar o mesmo caminho que usei, você deve
substituir o "digiteSeuUserAqui" pelo seu nome de usuário no Windows.
'''