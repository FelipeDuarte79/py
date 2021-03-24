# -*- coding: utf8 -*-

'''
#### TIPO REAL OU PONTO FLUTUANTE ####
- valor numérico do tipo real (float)
- pode ser tanto positivo como negativo
- a função float() permite converter um inteiro ou string em real
- sempre use float() para ler um real digitado pelo usuário, para operações
matemáticas, convertendo de string para real
- Python utiliza o ponto (.) como virgula decimal, separando a parte 
inteira da fracionária
'''

# Exemplo
print()
x = input('\tDigite um valor real para x: ')

print()
print(type(x))
x = float(x)
print(type(x))
