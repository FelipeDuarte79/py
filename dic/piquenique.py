#include -*- coding: utf8 -*-

convidados = {'Alice':{'maçãs':6, 'sanduíches':11},
              'Ricardo':{'bananas':9, 'pizza':5},
              'Silvia':{'maçãs':2, 'sucos':4},
              'Ana':{'laranjas':4, 'sanduíches':6},
              'Cássio':{'bananas':7, 'pizza':6},
              'Carlos':{'laranjas':8, 'sucos':15}}

def total_itens(convidados, item):
    c = 0    # contador
    for i, j in convidados.items():    # i (nomes), j (item:qtd)
        c = c + j.get(item, 0)    # metodo get() pega a quantidade e 0 p default
    return c

print(' - Maçãs: ' + str(total_itens(convidados, 'maçãs')))
print(' - Bananas: ' + str(total_itens(convidados, 'bananas')))
print(' - Laranjas: ' + str(total_itens(convidados, 'laranjas')))
print(' - Sanduíches: ' + str(total_itens(convidados, 'sanduíches')))
print(' - Pizza: ' + str(total_itens(convidados, 'pizza')))
print(' - Sucos: ' + str(total_itens(convidados, 'sucos')))
