"""
    EXERCÍCIO 12) Loop for e Lógica

    1. A partir da lista abaixo, faça:

    perguntas = [
        {
            'Pergunta': 'Quanto é 2+10?',
            'Opções': ['11', '8', '14', '12'],
            'Resposta': '12',
        },
        {
            'Pergunta': 'Quanto é 5*5?',
            'Opções': ['25', '55', '10', '51'],
            'Resposta': '25',
        },
        {
            'Pergunta': 'Quanto é 10/2?',
            'Opções': ['4', '5', '2', '1'],
            'Resposta': '5',
        },
    ]

    a) Exiba a pergunta e as opções de resposta ao usuário;
    b) Se o usuario acertar passe para a prox pergunta, caso contrario repita a pergunta
    c) Quando o usuario acertar todas as perguntas encerre o programa.

"""


perguntas = [
    {
        'Pergunta': 'Quanto é 2+10?',
        'Opções': ['11', '8', '14', '12'],
        'Resposta': '12',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for i in perguntas:
    print(i["Pergunta"])
    print(i["Opções"])
    resposta = input('Sua Resposta: ')

    while resposta != i["Resposta"]:
        print("Resposta Errada, tente novamente! ❌")
        resposta = input('Sua Resposta: ')

    print("Parabéns, você acertou! 👍🏻\n")

print('-- FIM DAS PERGUNTAS --')


"""
out:

Quanto é 2+10?
['11', '8', '14', '12']
Sua Resposta: 12
Parabéns, você acertou! 👍🏻

Quanto é 5*5?
['25', '55', '10', '51']
Sua Resposta: 51
Resposta Errada, tente novamente! ❌
Sua Resposta: 25
Parabéns, você acertou! 👍🏻

Quanto é 10/2?
['4', '5', '2', '1']
Sua Resposta: 5
Parabéns, você acertou! 👍🏻

-- FIM DAS PERGUNTAS --

"""