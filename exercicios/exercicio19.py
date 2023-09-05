"""
EXERCÍCIO 19) Função Recursiva

Funções recursivas, são funções que chamam a si mesmas durante sua execução. As funções recursivas são frequentemente usadas para resolver problemas que têm uma estrutura recursiva natural, 
sabendo disso, crie uma função para retornar o N-ésimo número na sequência de Fibonaci.

Dica:
A sequência de Fibonacci é uma das sequências matemáticas mais conhecidas e tem aplicações em várias áreas da matemática, ciência e computação. Ela também aparece em fenômenos naturais e em 
muitos contextos artísticos. A sequência pode ser definida matematicamente como: F(0) = 0 F(1) = 1 F(n) = F(n-1) + F(n-2) para n > 1 Onde F(n) representa o n-ésimo número na sequência de Fibonacci.
"""

def fibonacci(n):
    if n <= 0:  # base case
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # chamada recursiva

print(fibonacci(10))  # 55
print(fibonacci(1))  # 1
print(fibonacci(3))  # 2
