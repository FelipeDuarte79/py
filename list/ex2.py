# -*- coding: utf8 -*-
'''
EXERCÍCIO 2

'''

grade = [['.', '.', '0', '0', '.', '0', '0', '.', '.'],
         ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
         ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
         ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
         ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
         ['.', '.', '.', '.', '0', '.', '.', '.', '.']]


c = 0 # coluna
l = 0 # linha
while l < 6:
    c = 0
    while c < 9:
        if c == 8:
            print(grade[l][c], end='\n')
        else:
            print(grade[l][c], end='')
        c += 1
    l += 1