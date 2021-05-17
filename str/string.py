# -*- coding: utf8 -*-

'''
#### TIPO CARACTERE ####
- strings na verdade são nada mais que caracteres em cadeia
- a função str() permite converter um qualquer tipo de dados em string
- a função input (Python3.x) e raw_input (Python2.x) sempre retorna uma string
- o operador + permite concatenar strings
- o operador * permite repetir strings
- como strings na verdade são cadeias de caracteres, cada caractere possui um
índice
- o primeíro elemento sempre terá índice 0
- uma strings de n caracteres, o último elemento sempre terá índice n-1
- você pode referenciar o último elemento, penúltimo, antepenúltimo como:
[-1], [-2], [-3] (respectivamente)
- uma string pode ser fatiada em pedaços (slices)
- toda a string pode ser referida como [inicio:parada:incremento]
- string pode ser referida parcialmente como [3:5]
'''

# Exemplo
print()
x = 'Python é uma linguagem de porgramação muito versátil!'

print()
print('\t %s' % (type(x)))
print('\t' + x)
print('\t' + x + x)
print('\t' + x * 3)
print('\t' + x[:])         # toda a string 
print('\t' + x[0])         # o primeiro caractere
print('\t' + x[-1])        # o último caractere
print('\t' + x[-2])        # o penuúltimo caractere
print('\t' + x[-3])        # o antepúltimo caractere
print('\t' + x[4:-2])      # do índice 4 ao penúltimo caractere 
print('\t' + x[::5])       # toda a string, a cada cinco caracteres
