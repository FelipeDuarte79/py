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
- uma string inicia e termina com aspas simples e duplas
- se necessário usar aspas simples dentro de uma string, você têm duas opções:
- usar aspas duplas: "exemplo de aspas simples: '"
- por usar caractere de escape: 'exemplo de aspas simples: \''
- Python utiliza os seguintes caracteres de escape:
    \': aspas simples
    \": aspas duplas
    \t: tabulação
    \n: nova linha
    \\: barra invertida
- string pura (raw string): ignora qualquer caractere de escape e trata tudo
exatamente como caracteres: r'Exemplo:'
- é possível utilizar docstring
- lembre que # é utilizando para comentários de uma ou meia linha
- três aspas simples ou duplas é utilizado para docstrings
- é possível verificar se um caratere está na string por meio do operador in
- é possível verificar se um caratere não está na string por meio do operador
not in

#### MÉTODOS ÚTEIS ####
.upper(): converte a string para maiúscula
.lower(): converte a string para minúscula
.title(): converte a string  para o formato título (primeira letra de cada
palavra em maiuscula)
.isupper(): verifica se existe caractere maiúsculo
.islower(): verifica se existe caractere minúsculo
.isaplha(): verifica se a string é constituída apenas de letras e não vazia
.isalnum(): verifica se a string é constituída apenas de letras, números e não
vazia
.isdecimal(): verifica se a string é constituída apenas de caracteres numéricos
e não nula
.isspace(): verifica se a string é constituida apenas de espaços em branco,
tabulações, quebra de linhas,e não vazia
.istitle(): rifica se a string contém o primeiro caracteres maiúsculo e as
.startswith(): verifica se a string inicia com o parâmetro iniciado
.endswith(): verifica se a string inicia com o parâmetro iniciado
.join(): une uma lista de strings (passada como parâmetro) em uma única string.
O objeto é o caractere separador entre as palavras.
.split(): faz justamente o contrário, extrai as palavras do objeto e converte em
uma lista. O argumento serve como separador se for usado.
.rjsut(): alinhamento à direita, a função aceita dois parâmetros opcionais:
número de casas, e o caractere utilizado para distaciamento
.ljust(): semelhante a .rjust() porém, alinhado à esquerda
.center(): semelhante a .rjust() porém, alinhado ao centroà
.strip(): remove os espaços em branco, se passado como parâmetro 
.rstrip(): remove os espaços em branco à direita
.lstrip(): remove os espaços em branco à esquerda
.pyperclip(): 
'''

# EXEMPLOS
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
print('\t' + x[-2])        # o penultimo caractere
print('\t' + x[-3])        # o antepúltimo caractere
print('\t' + x[4:-2])      # do índice 4 ao penúltimo caractere 
print('\t' + x[::5])       # toda a string, a cada cinco caracteres
print('Exemplo utilizando aspas simples \'')
print('Exemplo utilizando aspas simples e duplas\"')
print("Exemplo utilizando aspas duplas\"")
print("Exemplo utilizando aspas duplas e simples\'")
print('\tExemplo de tabulação')
print('\nExemplo de nova linha')
print('Exemplo de barra invertida: \\')
print(r'Exemplo de string pura (raw string) \t \n \\ \' \"')
print('''
Exemplo utilizando

             docstring com 
                                   aspas simples''')
print("""Exemplo de string 

utilizando docstring
                           com aspas duplas""")
print('P' in 'Python')
print('p' in 'Python') # p é diferente P
print('P' not in 'Python')
print('p' not in 'Python')
print('Python'.upper())
print('Python'.lower())
print('python'.islower())
print('Python'.islower())
print('PYTHON'.isupper())
print('Python'.isupper())
print('Python'.lower().islower())
print('Python'.upper().isupper())
print(''.isalpha())
print(' '.isalpha())
print('P y t h o n '.isalpha())
print('Python'.isalpha())
print('Python123'.isalpha())
print('Python!@#$'.isalpha())
print('!@#$'.isalpha())
print(''.isalnum())
print(' '.isalnum())
print(' P y t h o n '.isalnum())
print('Python'.isalnum())
print('Python123'.isalnum())
print('123'.isalnum())
print('123asjkds'.isdecimal())
print('123  '.isdecimal())
print('123'.isdecimal())
print(''.isspace())
print(' '.isspace())
print('\t'.isspace())
print('\n'.isspace())
print('	'.isspace())
print('python é legal'.title())
print('Python é legal'.istitle())
print('Python É legal'.istitle())
print('Python É Legal'.istitle())
print('Python '.startswith('P'))
print('Python '.startswith('p'))
print('\t'.startswith('\t'))
print(''.startswith(''))
print('Python'.endswith(''))
print('Python '.endswith(' '))
print('Python\n'.endswith(' '))
print('Python\n'.endswith('\n'))
print(', '.join(['cats', 'bats', 'hats']))
print('cats bats hats'.split())
print('catsbatshats'.split('s'))
print('Python'.rjust(20))
print('Python'.rjust(20, '#'))
print('Python'.ljust(20, '#'))
print('Python'.center(20, '#'))
print('  Python  Python  '.strip('  thonPy  '))
print('  Python  Python  '.strip())
print('  Python  Python  '.rstrip())
print('  Python  Python  '.lstrip())

import pyperclip as pc    # deve ser instalado com o pip
pc.copy('Hello world!!!')
pc.paste()
