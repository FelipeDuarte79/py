# -*- coding: utf8 -*-

'''
#### TIPO INTEIRO ####
- valor numérico do tipo inteiro (int)
- pode ser tanto positivo como negativo
- a função int() permite converter um real ou string em inteiro
- sempre use int() para ler um inteiro digitado pelo usuário, para operações
matemáticas, convertendo de string para inteiro
'''

# Exemplo
print()
x = input('\tDigite um inteiro para x: ')

print()
print(type(x))
x = int(x)
print(type(x))