"""
EXERCÍCIO 4) List Comprehension:

    Dada a lista de produtos:

        produtos = [
        {'nome': 'Arroz 5kg', 'valor': 21.90},
        {'nome': 'Feijão Preto 1kg', 'valor': 7.80},
        {'nome': 'Peito Frango 1kg', 'valor': 13.50},
        {'nome': 'Ovo 30u', 'valor': 19.90},
        {'nome': 'Farinha de Trigo 1kg', 'valor': 4.90},
        ]

    1. Gere uma nova list, usando list comprehension com aumento de 5% nos produtos que possuirem o valor abaixo de R$ 15,00.
"""


produtos = [
    {'nome': 'Arroz 5kg', 'valor': 21.90},
    {'nome': 'Feijão Preto 1kg', 'valor': 7.80},
    {'nome': 'Peito Frango 1kg', 'valor': 13.50},
    {'nome': 'Ovo 30u', 'valor': 19.90},
    {'nome': 'Farinha de Trigo 1kg', 'valor': 4.90},
]

precos_atualizados = [
    {**item, 'valor': round(item['valor'] * 1.05, 2)} if item['valor'] < 15 else {**item} for item in produtos
]

print(*precos_atualizados, sep='\n')

"""
output:
{'nome': 'Arroz 5kg', 'valor': 21.9}
{'nome': 'Feijão Preto 1kg', 'valor': 8.19}
{'nome': 'Peito Frango 1kg', 'valor': 14.18}
{'nome': 'Ovo 30u', 'valor': 19.9}
{'nome': 'Farinha de Trigo 1kg', 'valor': 5.15}
"""
