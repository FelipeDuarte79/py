# -*- coding: utf8 -*-

'''
#### IMPORTANDO MÓDULOS ####
- todo programa pode chamar funções internas (built-in)
- existe também um conjunto de bibliotecas padrão
- há diversas maneiras de importar uma biblioteca

#### FUNÇÕES ÚTEIS ####
random.randint(): faz um sorteio aleatório de um número inteiro 
range(): gera uma lista de números inteiros
sys.exit(): esta função permite encerrar um programa quando este chega ao fim
das instruções. Essa função é importada do módulo sys
'''

# Exemplo
from math import *
from math import pi
from math import pi as numeroPI
import math, pandas, random, sys

print()

print(random.randint(10,50))

print()

print(*range(0,20,3))
sys.exit()
