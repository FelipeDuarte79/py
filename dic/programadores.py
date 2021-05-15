# -*- coding: utf8 -*-

programadores = {'Beatriz': {'C':4, 'Python':3},
                 'Régis':   {'PHP':5, 'Java':4},
                 'Clóvis':  {'Python':4, 'Java':6},
                 'Jonas':   {'Cobol':9, 'C++':7},
                 'Ana':     {'GO':3, 'Raskel':2},
                 'josé':    {'Java':9, 'Javascript':5},
                 'Cássio':  {'Shell Script':7, 'Go':3},
                 'Eduardo': {'Raskel':6, 'C++':9},
                 'Gabriel': {'Assembly':7, 'Java':7},
                 'Matheus': {'Python':6, 'Assembly':4},
                 'Carla':   {'Cobol':5, 'Assembly':4},
                 'Estele':  {'Assembly':7, 'Delphi':4},
                 'Clarice': {'C':5, 'PHP':4}}

def resumo(equipe, item):
    c = 0    # tempo total 
    for i, j in equipe.items():
       c = c + j.get(item, 0)    # .get(item) pega o número (anos)
    return c

print('- C: ' + str(resumo(programadores, 'C')))
print('- Python: ' + str(resumo(programadores, 'Python')))
print('- PHP: ' + str(resumo(programadores, 'PHP')))
print('- Java: ' + str(resumo(programadores, 'Java')))
print('- Cobol: ' + str(resumo(programadores, 'Cobol')))
print('- C++: ' + str(resumo(programadores, 'C++')))
print('- GO: ' + str(resumo(programadores, 'GO')))
print('- Raskel: ' + str(resumo(programadores, 'Raskel')))
print('- Javascript: ' + str(resumo(programadores, 'Javascript')))
print('- Shell Script: ' + str(resumo(programadores, 'Shell Script')))
print('- Assembly: ' + str(resumo(programadores, 'Assembly')))
