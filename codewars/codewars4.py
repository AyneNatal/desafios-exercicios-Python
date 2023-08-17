"""
-> Desafio: Name on billboard (8 Kyu)
-> Link para o desafio no site: https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/python

Instructions:
You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of £30,
but that can be different if you are given 2 parameters instead of 1 (allways 2 for Java).

You CAN NOT use multiplier "*" operator.

If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a character).
"""


import math

def billboard(name, price=30):
    return math.prod([len(name), price])

# Tests:
print(billboard('Jeong-Ho Aristotelis'))  # out: 600
print(billboard('Abishai Charalampos'))  # out: 570
