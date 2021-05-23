#!/usr/bin/env python3
# -*- coding: utf8 -*-




'''
#### OPERADORES MATEMÁTICOS ####
- exponencial: **
- módulo ou resto: %
- divisão inteira: //
- divisão: /
- multiplicação: *
- subtração: -
- adição: +


#### PRECEDÊNCIA DOS OPERADORES ####
()
**
* / // %
+ -
da esquerda para a direita
'''




# EXEMPLOS

print('\n\tDIGITE OS VALORES\n\t#################\n')
x = int(input('\tx (menor): '))    # DIGITE UM NÚMERO MENOR
y = int(input('\ty (maior): '))    # DIGITE UM NÚMERO MAIOr

print()
print('\t%d ** %d = %d' % (y, x, y ** x))    # EXPONENCIAL
print('\t%d %% %d = %d' % (y, x, y % x))     # MÓDULO
print('\t%d // %d = %d' % (y, x, y // x))    # DIVISÃO INTEIRA
print('\t%d / %d = %d' % (y, x, y / x))      # DIVISÃO
print('\t%d * %d = %d' % (y, x, y * x))      # MULTIPLICAÇÃO
print('\t%d + %d = %d' % (y, x, y + x))      # ADIÇÃO
print('\t%d - %d = %d' % (y, x, y - x))      # SUBTRAÇÃO
print('\n\n')
