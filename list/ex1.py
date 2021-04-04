# -*- coding: utf8 -*-
'''
EXERCÍCIO 1
Crie uma função que aceite uma lista como argumento e retorne uma string com
todos os itens separados por uma vírgula, espaço com um e, antes do último item,
um ponto final na última palavra e os caracteres de nova linha e tab no primeiro
elemento
'''


frutas = ['uva', 'banana', 'abacaxi', 'maçã', 'pera', 'morango', 'laranja']

def cesta(frutas):
    t = len(frutas)
    for e, fruta in enumerate(frutas):
       if e == 0:
           print('\n\t' + fruta, end=', ')
       if e > 0 and e < t - 2:
           print(fruta, end=', ')
       if e == t - 2:
           print(fruta, end=' ')
       if e == t -1:
           print('e '+ fruta + '.\n')

cesta(frutas)
