#!/usr/bin/env python3
# para Linux, é necessário ter instalado o pacote xclip
# include -*- coding: utf8 -*-

import sys, pyperclip

passwords = {'gmail':'abc',
             'hotmail':'123'
              }

if len(sys.argv) < 2:
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(account + ' copiado para colar')
else:
    print(account + ' não encontrado')
