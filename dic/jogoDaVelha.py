# -*- coding: utf8 -*-


rodada = {'0':' ', '1':' ', '2':' ',
          '3':' ', '4':' ', '5':' ',
          '6':' ', '7':' ', '8':' '}

def quadro(rodada):
    print('\n\t' + rodada['0'] + '|' +  rodada['1'] + '|' +  rodada['2'])
    print('\t' + '-+-+-')
    print('\t' + rodada['3'] + '|' +  rodada['4'] + '|' +  rodada['5'])
    print('\t' + '-+-+-')
    print('\t' + rodada['6'] + '|' +  rodada['7'] + '|' +  rodada['8'] + '\n')

print('\n\t0|1|2\n\t-+-+-\n\t3|4|5\n\t-+-+-\n\t6|7|8')
quadro(rodada)

var = 'X'
c = 0
while c <= 8:
    print('Jogador %s, escolha a casa: ' % (var))
    casa = input()

    if casa == '0' and var == 'X':
        rodada['0'] = 'X'
    elif casa == '0' and var == 'O':
        rodada['0'] = 'O'
    elif casa == '1' and var == 'X':
        rodada['1'] = 'X' 
    elif casa == '1' and var == 'O':
        rodada['1'] = 'O'
    elif casa == '2' and var == 'X':
        rodada['2'] = 'X'
    elif casa == '2' and var == 'O':
        rodada['2'] = 'O'
    elif casa == '3' and var == 'X':
        rodada['3'] = 'X'
    elif casa == '3' and var == 'O':
        rodada['3'] = 'O'
    elif casa == '4' and var == 'X':
        rodada['4'] = 'X'
    elif casa == '4' and var == 'O':
        rodada['4'] = 'O'
    elif casa == '5' and var == 'X':
        rodada['5'] = 'X'
    elif casa == '5' and var == 'O':
        rodada['5'] = 'O'
    elif casa == '6' and var == 'X':
        rodada['6'] = 'X'
    elif casa == '6' and var == 'O':
        rodada['6'] = 'O'
    elif casa == '7' and var == 'X':
        rodada['7'] = 'X'
    elif casa == '7' and var == 'O':
        rodada['7'] = 'O'
    elif casa == '8' and var == 'X':
        rodada['8'] = 'X'
    elif casa == '8' and var == 'O':
        rodada['8'] = 'O'
    c += 1



    quadro(rodada)



    if var == 'X':
        var = 'O'
    else:
       var = 'X'
        
