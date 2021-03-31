# -*- coding: utf8 -*-
'''
#### FUNÇÕES ####
- funções são programas menores dentro de um programa maior
- as regras para nome de variáveis são as mesmas para funções
- sua sintaxe é: def nome_da_funçã0():
- um dos propósitos das funções é agrupar códigos que seriam escrito diversas
vezes, poupando assim serviço, código e tempo
- corrigir bugs é mais fácil em funções do que ficar procurando em um programa
que pode ter centenas de linhas de código
- a instrução def pode receber um parâmetro (argumentos da função) 
- os parâmetros de uma função só existem dentro desta logo, quando a função é
encerrada estes valores serão descartados
- ao criar uma função, podemos especificar qual será o valor de retorno com a
instrução return seguido do valor
- em Python, há um valor chamado None, que representa a ausência de um valor e o
seu tipo é NoneType
- argumentos nomeados são identificados pela palavra-chave inseridas antes deles
na chamada da função
- a função print possui dois parâmetros opcionais para exibir: end (final) e sep 
(separador)
- cuidado ao utilizar valores padrões para dados do tipo mutáveis
- escopo local é o local onde as variáveis e os parâmetros são atribuídos dentro
de uma função. Um escopo local é criado sempre que uma função é chamada.
Qualquer variável que recebe um valor nessa função existirá no escopo local.
Quando a função retornar, o escopo local será destruído e essas variáveis
esquecidas.
- escopo global é a atribuição de variáveis fora de qualquer função. Existe
apenas um escopo global e ele é criado quando o programa inicia
- variável local não podem ser usadas no escopo global
- variáveis são restritos aos seus escopos locais
- variáveis globais podem ser lidas por escopos locais
- o prefixo da instrução global, permite que esta seja uma variável global em
qualquer lugar do código, independente de escopo
- funções lambda são mini-funções anônimas
- sua sintaxe é: nome = lambda var1, var2: expressão
'''

# Exemplos
import random

print()

# EXEMPLO 0: usando end e sep da função print
msg = 'Python é fácil de programar'
print(msg,end='!')

print() 

# EXEMPLO 1: uma função simples que não recebe nenhum argumento e retorna nada
def exemplo1(): 
    print('ok')
exemplo1()

print()

# EXEMPLO 2: uma função que retorna valor um valor aleatório
def exemplo2(): 
     return random.randint(0,10)
print(exemplo2())

print()

# EXEMPLO 3: uma função que recebe um valor aleatório como parâmetro e soma com
# outro e retona
def exemplo3(y):
    x = random.randint(0,50)
    print(y, x)
    return  y + x
print(exemplo3(random.randint(0,10)))

print()

# EXEMPLO 4: uma função que que possui um parâmetro default 
def exemplo4(y = 8, x = 5):
    print(x, y)
    return (x / y)
print(exemplo4(y = 5, x = 20))
print(exemplo4(y = 2))
print(exemplo4(x = 2))
print(exemplo4())

print()

# EXEMPLO 5: cuidado com dados mutaveis, atente que a lista  nunca é limpa, isso
# acontece porque o Python não cria uma lista vazia a cada chamada da função por
# questão de otimização, reaproveitando a lista que uma vez foi criada
def exemplo5(lista = []):
    lista.append(random.randint(0,100))
    return lista
print(exemplo5())
print(exemplo5())
print(exemplo5())
print(exemplo5())

print()

# EXEMPLO 6: corrigindo o problema anterior atribuindo o valor None ou []
def exemplo6(lista = None):
    lista = lista or []
    lista.append(random.randint(0,100))
    return lista
print(exemplo5())
print(exemplo5())
print(exemplo5())
print(exemplo5())

print()

# EXEMPLO 7: mini-função com def
def exemplo7(x): return x**2
print(exemplo7(random.randint(0,100)))

print()

# EXEMPLO 8: função lambda
x = random.randint(0,20)
y = random.randint(0,10)
f_lambda = lambda x, y: x ** y
print(f_lambda(x,y))
