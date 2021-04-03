# -*- coding: utf8 -*-

'''
#### TIPO TUPLA ####
- tupla é muito semelhante à lista porém como a string, a tupla não pode ser
alterada 
- como consequência, você não pode alterar, deletar ou adicionar elementos em
uma nova tupla
- para valores imutaveis como tupla e string, a própria variável armazena o
valor
- enquanto a lista utiliza [], a tupla utiliza ()
- para um ou mais valores, utilize: ('dados', ) (sim uma virgula mesmo para
apenas um elemento)
'''

print()

# EXEMPLO 0: erro ao adicionar tupla
tupla = (1,) 
def adicionaTupla():
    try:
        tupla.append(2)
    except AttributeError:
        return 'Impossivel adicionar informação na Tupla'

print(adicionaTupla())

print()

# EXEMPLO 1: erro ao deletar tupla
tupla = (1,) 
def deletaTupla():
    try:
        tupla.pop(0)
    except AttributeError:
        return 'Impossivel deletar informação da Tupla'

print(deletaTupla())

print()

# EXEMPLO 1: copiando dados da lista para a tupla
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8) 
lista = list(tupla)
print(lista)
lista.append(9)
lista.pop(0)
print(lista)
