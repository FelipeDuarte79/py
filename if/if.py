# -*- coding: utf8 -*-
import random

'''
#### CONDICIONAL IF ####
- instruções de controle de fluxo iniciam com uma condição
- toda condição são seguidas por blocos de código (cláusula)
- condição é avaliado como um valor booleano que possui apenas um valor: True
ou False
- as linhas de código Python podem ser agrupadas em blocos
- um bloco começa e termina a partir da indentação das linhas de código

#### INSTRUÇÃO IF ####
- esta cláusula é obrigatória e deve haver pelo menos uma
- a cláusula de uma instrução if será executada se a condição for True

#### INSTRUÇÃO ELSE ####
- esta cláusula é opcional e única
- a cláusula else será executada somente quando a condição da instrução if for
false

#### INSTRUÇÃO ELIF ####
- a instrução elif é uma instrução else-if, que sempre vem após um else
- esta provê outra condição que só será executada, se todas as anteriores forem
falsas

'''

# Exemplo

var = random.randint(0,15)


if var <= 2:
    print('O valor é digitado menor ou igual à cinco.')


if var <= 5:
    print('O valor digitado é menor ou igual à cinco.')
else:
    print('O valor é digitado é maior do que cinco.')

if var <= 2:
    print('O valor está entre 0 e 2')
elif var >= 3 or var <= 5:
    print('O valor está entre 3 e 5')
elif var >= 6 or var <= 9:
    print('O valor está entre 6 e 9')
else:
    print('O valor é maior que 9.')
