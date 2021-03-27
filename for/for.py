# -*- coding: utf8 -*-

'''
#### LAÇO DE REPETIÇÃO FOR ####
- 
'''

# Exemplo

for i in range(34,67,3):                      # exemplo com inteiros
    print(i)

print()

nomes = ['Ana', 'Bia', 'Zé', 'JP']       # exemplo com strings
for nome in nomes:
    print(nome)

print()

x = [0, 3, 6]
y = [1, 4, 7]
z = [2, 5, 8]
for i, j, k in zip(x, y, z):             # exemplo utilizando 3 variáveis
    print(i, j, k)

print()

lista = [item * 4 for item in range(10)] # lista de compreensão
print(lista)
