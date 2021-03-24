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

# Exemplo

print('\n')
x = int(input('x (menor): '))
y = int(input('y (maior): '))

print()
print('\t%d ** %d = %d' % (y, x, y ** x))
print('\t%d %% %d = %d' % (y, x, y % x))
print('\t%d // %d = %d' % (y, x, y // x))
print('\t%d / %d = %d' % (y, x, y / x))
print('\t%d * %d = %d' % (y, x, y * x))
print('\t%d + %d = %d' % (y, x, y + x))
print('\t%d - %d = %d' % (y, x, y - x))
print('\n\n')
