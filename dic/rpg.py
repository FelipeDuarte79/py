# include -*- coding: utf8 -*-

inventario = {'corda':2,
              'tochas':3,
              'moedas':96,
              'flechas':9}

def configura(chave, valor):
    inventario[chave] = valor

def exibe(invent):
    print('\n\tINVENTÁRIO\n\t##########\n')
    for i, j in invent.items():
        print('\t' + str(i) + ': ' + str(j) + '')
    print('\n\n')

def exibe_menu():
    return '''\n\t0 = adiciona item
        1 = exibe inventárioa
        *** Enter para sair ***'''

while True:
    print(exibe_menu())
    opcao = input('\n\tDigite a opção: ') 
    if opcao == '':
        break
    elif opcao == '0':
        item = input('\n\tDigite o item a ser adiconado: ')
        valor = input('\tDigite a quantidade: ')
        configura(item, valor)
    elif opcao == '1':
        exibe(inventario)
