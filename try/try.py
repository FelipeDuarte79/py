# -*- coding: utf8 -*-

'''
#### TRATAMENTO DE EXCEÇÕES ####
- obter um erro e exceção são sinônimos
- exemplos de exceção: divisão por zero, entrada de dados inesperados
- o erros podem ser tratados com as instruções try e except
- o código que pode conter um erro em potencial é inserido na cláusula try
- a execução do programa segue para a cláusula except, caso o erro ocorra
- uma lista de except pode ser obtida em:
https://docs.python.org/3/library/exceptions.html
'''


print()

# EXEMPLO 1: erro: divisão por zero 
import random
y = random.randint(0,10)
x = random.randint(0,100)
def exemplo1(x,y): 
    try:
        return x / y
    except ZeroDivisionError:
        return 'Erro!!!! Divisão por zero.'
print(exemplo1(x,y))

print()

# EXEMPLO 2: esperado uma string, não um inteiro
var = int(input('Digite a sua idade: '))
def exemplo2(var):
    try:
        print('Idade' +  var)
    except TypeError:
        return 'Esperado uma string, não um inteiro'

print(exemplo2(var))
