#!/usr/bin/env python3
# -*- coding: utf8 -*-




'''
#### TIPO INTEIRO ####
- valor numérico do tipo inteiro (int)
- pode ser tanto positivo como negativo
- a função int() permite converter um real ou string em inteiro
- sempre use int() para ler um inteiro digitado pelo usuário, para operações
matemáticas, convertendo de string para inteiro
'''




# EXEMPLOS

x = input('\tDigite um inteiro para x: ')    # A FUNÇÃO INPUT SEMPRE RETORNA UMA
# STRING

print()
print(type(x))    # TIPO STRING
x = int(x)        # CONVERSÃO DE STRING PARA INT
print(type(x))    # TIPO INTEIRO
