"""
EXERCÍCIO 8) Dicionários

    A partir do dicionário a seguir:
    my_dict = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964,
        'price': 50000.00,
        'colors': [
            {'primary_color': 'black'},
            {'secondary_color': 'white'}
        ]
    }

        1. Altere o valor do carro para R$55000,00 e o ano para 1965.
        2. Acrescente uma terceira cor na chave 'colors'.
        3. Exclua a marca (brand).
        4. Imprima o novo dicionário com uma chave abaixo da outra.


"""

my_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    'price': 50000.00,
    'colors': [
        {'primary_color': 'black'},
        {'secondary_color': 'white'}
    ]
}

# 1)
my_dict.update({
    'year': 1965,
    'price': 55000.00
})

# 2)
my_dict['colors'].append({'third': 'gray'})

# 3)
my_dict.pop('brand')

# 4)
for key, value in my_dict.items():
    print(f'{key}: {value}')


"""
output:

model: Mustang
year: 1965
price: 55000.0
colors: [{'primary_color': 'black'}, {'secondary_color': 'white'}, {'third': 'gray'}]

"""

