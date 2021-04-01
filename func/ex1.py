# -*- coding: utf8 -*-

# CRIE UMA FUNÇÃO QUE CALCULE A SEQUÊNCIA COLLATZ

def collatz(n):
    if n % 2 == 0:
        return (n // 2)
    else:
        return (3 * n + 1)

x = int(input('Digite um inteiro: '))

while x > 0:
    x = collatz(x)
    print(x)
    if x == 1:
        break
