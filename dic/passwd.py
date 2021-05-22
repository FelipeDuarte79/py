#!/usr/bin/env python3
# include -*- coding: utf8 -*-
# um programa para gerenciar suas senhas

import sys, pyperclip as pc

passwd = {}    # BANCO DE SENHAS


def nome(): return input('\tNome: ')
def senha(): return input('\tSenha: ')


def menu():    # 0 - EXIBE MENU
    print('''\t0 - exibe menu
       \t1 - consulta 
       \t2 - cadastra
       \t3 - copia 
       \t\u21B5 - sai''')


def consulta():   # 1 CONSULTA SENHA
    return '\tSua senha é: ' + passwd.get(nome()) 


def cadastro():    # 2 - CADASTRA NOME E SENHA
    nome = input('\tNome: ')
    if nome != '':
       passwd[nome] = str(input('\tSenha: '))
       return '\tNome de usuário e senha cadastrado com sucesso!!!'


def copia():    # 3 - COPIA A SENHA
    nomeV = nome()
    senha = passwd.get(nomeV)
    pc.copy(senha)
    return '\tSenha copiada'



print()
retorno = ' '
menu()

while True:
    funcao = input('\n\tDigite a sua opção: ')

    if funcao == '0':
        menu() 
    elif funcao == '1':
       retorno = consulta()
    elif funcao == '2':
       retorno = cadastro()
    elif funcao == '3':
       retorno = copia()
    else:
       print('\tSaindo ...')

    print(retorno)
    if retorno == '' or funcao == '':
        sys.exit()
