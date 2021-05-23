# -*- coding: utf8 -*-




'''
#### TIPO BOOLEANO ####
- valores booleano possuem apenas um valor de dua opções: verdadeiro ou falso
- True (verdadeiro)
- False falso)

# Operadores lógicos
- and (e)
- or (ou)
- not ((negação)

# Operadores relacionais
- ==  (igual)
- !=  (diferente)
- <   (menor que)
- <=  (menor ou igual)
- >   (maior que)
- >=  (maior ou igual)

# Observações
- Os valores 0 (zero inteiro), 0.0 (zero real) e '' (string vazia) são
considerados False. Qualquer valor fora disso é considerado True
'''




# EXEMPLOS

# Operadores lógicos
print(not True)
print(not False)
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

# Operadores relacionais
print(True == True)
print(False == True)
print(True != True)
print(False != True)
print(True < True)
print(True <= True)
print(False > False)
print(True >= False)

# Outros tipos de dados
print(0 == 0.0)
print(0 == 3)
int('' == 'a')
