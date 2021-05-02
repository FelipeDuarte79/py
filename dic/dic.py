# -*- coding: utf8 -*-

'''
#### TIPO DICIONARIO ####
- tipo de dado que pode agrupar diversos tipos de valores
- os índices nos dicionários são chamados chaves (keys)
- para cada chave, existe um valor (value)
- uma chave com seu valor, é chamado de par chave-valor (key-value pair)
- um dicionário é criado utilizando um par de chaves 
- o operador in verifica se a chave existe no dicionário
- mas o operador in não consegue verificar valores das chaves

#### MÉTODOS ####
- .keys(): permite obter as chaves do dicionário
- .value(): permite obter os valores das chaves
- .items(): permite obter o par chave-valor
- .setdefault(): permite criar um par padrão para o dicionário

#### APRESENTAÇÃO ELEGANTE
- o modulo pprint permite acesso a função úteis tais como:
pprint() pformat(): uma apresentação elegante dos valores de um dicionario
'''

print()

# EXEMPLO 0: 
cars = {'ford':'mustang', 'chevrolet':'camaro', 'bmw':'M4', 'audi':'TT',
'honda':'acord'}
print(cars)

print('ford' in cars) # operador in funciona com chaves
print('mustang' in cars) # mas o operador in não funciona com valores
cars['porshe'] = 911 # adicionando a chave 'porshe' e o valor '911'
print(cars)

print()

print(cars.keys())
print(cars.values())
print(cars.items())

print()

print('mustang' in cars.values())# verificando se o valor existe no dicionario
print('volkwagem' in cars.keys())# verificando se a chave existe no dicionario
print(cars.get('bmw')) # o metodo get, retorna o valor quando a chave é passado
# como argumento

cars.setdefault('McLaren','speedtail') # o padrão McLaren é definido como
# carro padrão e a o valor é speedtail
print(cars)
cars.setdefault('McLaren','F1') # o valor padrão já foi definido e não pode ser
# alterado
print(cars)

print()

from pprint import pprint, pformat
pprint(cars)
