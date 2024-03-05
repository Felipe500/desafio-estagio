"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
 ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código
"""

n = int(input("Que termo deseja encontrar: "))

def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        next_number = sequencia[-1] + sequencia[-2]
        sequencia.append(next_number)
    return sequencia


fibonacci_sequencia = fibonacci(n)
if n in fibonacci(n):
    print(f'{n} está na sequencia de fibonacci \n {fibonacci_sequencia}')
else:
    print(f'{n} não está na sequencia de fibonacci \n {fibonacci_sequencia}')

