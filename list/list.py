# -*- coding: utf8 -*-

'''
#### TIPO LISTA ####
- tipo de dado que pode contém diversos dados podendo ser iguais ou diferentes
tipos de informação
- esta sequência é ordenada e possui um índice paraca cada elemento
- cada elemento é separado por vírgula 
- o índice é representado por um inteiro podendo ser positivo: 0 (primeiro), 1
(segundo), 3 (terceiro)
- ou negativo: -1 (último), -2 (penúltimo), -3 (antepenúltimo)
- para acessar fatias (slices) você pode utilizar a sintaxe [i:j]
- se i for omitido, por padrão Python pega do ínicio da lista
- se j for omitido, por padrão Python pega do fim da lista
sintaxe: [inicio:parada:incremento]
- assim como existe o operador in para verificar se a palavra existe na lista,
também existe o operador not in, para verificar se a palavra não está na lista 
- método é uma função que deve ser executada sobre um valor deste modo, temos
alguns métodos tais como:
- .index(argumento): o argumento é o dado que deve ser verificado na lista e
caso este exista, ele retorna com o índice
- .append('argumento): este método sempre adicionará um novo elemento no final 
da lista
- .inser(i,argumento): este método adiciona o argumento na posição i
- .remove(argumento): este método remove o argumento da lista. Se o elemento
existe diversas vezes, o método terá que ser executado tantas vezes quanto for
necessário até o elemento repetido ser deletado completamente
- .sort(): ordena e altera a ordem de uma lista 
- .pop(i): remove o elemento com índice i e armazena em uma variável
- .clear(): remove todos os elementos
- .copy(): copia os elementos
- .count(): conta o número de elementos
- .extend(): adiciona todos os elementos de uma lista no final
- .reverse(): lista em ordem reversa da original
- o caractere \ permite que instruções muito compridas, sejam quebradas em tantas
linhas quanto forem necessário
'''

print()

# EXEMPLO 0: lista de frutas
cesta = ['uva', 'pera', 'maçã', 'kiwi']
for fruta in cesta:
    print(fruta)

print()

# EXEMPLO 1: criando uma lista numerada de frutasc
cesta = ['uva', 'pera', 'maçã', 'kiwi']
for fruta in enumerate(cesta):
    print(fruta)

print()

# EXEMPLO 2: acessando as frutas pelo índice numerado
cesta = ['uva', 'pera', 'maçã', 'kiwi']
t = len(cesta)
for i in range(t):
    print(cesta[i])

print()

# EXEMPLO 3: acessando as frutas pelo índice negativo
cesta = ['uva', 'pera', 'maçã', 'kiwi']
t = (len(cesta) * -1)
i = -1
while i >= t:
    print(cesta[i])
    i -= 1

print()

# EXEMPLO 4: acessando fatias 
cesta = ['uva', 'pera', 'maçã', 'kiwi', 'mertilo', 'morango', 'laranja']
print(cesta[:]) # toda a lista
print(cesta[::2]) # toda a lista a cada dois elementos
print(cesta[1:5]) # do segundo ao sexto
print(cesta[:2]) # do início ao primeiro
print(cesta[1:]) # do segundo ao final
print(cesta[::-1])# acessando toda a lista em ordem inversa
cesta[2] = 'jaca' # substituindo um elemento por um novo
cesta[-1] = cesta[2] # substituindo um elemento por outro já existente
print(cesta[:])
cesta0 = cesta[:] + ['laranja', 'kiwi'] # adicionando novos elementos
print(cesta0)
cesta0 + ['laranja', 'kiwi']
del cesta0[2] # deletando o terceiro elemento
print(cesta0)
print(cesta0.index('laranja')) # vericando se o argumento está na lista
cesta0.append('melancia') # adicionado o argumento na lista
print(cesta0)
cesta0.insert(2,'melão') # insere o elemento melão no índice 2
print(cesta0)
cesta0.remove('melão') # remove o elemento melão
print(cesta0)
cesta0.sort() # ordena a lista
print(cesta0)
excluido = cesta0.pop(3) # exclui o elemento de índice 3 e armazena seu conteúdo
print(excluido)
