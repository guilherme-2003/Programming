import pandas as pd
from datetime import datetime
import numpy as np

tabela = pd.read_excel('Contabilidade.xlsx')
mes_atual = datetime.today().strftime('%B') 

lista_total_credito = []

def substitui_valores():
    tabela['VALOR A RECEBER'].fillna(0.0, inplace=True)
    tabela['VALOR A PAGAR'].fillna(0.0, inplace=True)
    tabela['PARCELA'].fillna(0.0, inplace=True)
    tabela['TOTAL PARCELAS'].fillna(0.0, inplace=True)
    tabela['CREDOR'].fillna('Dívida sem credor', inplace=True)
    tabela['DEVEDOR'].fillna('Dívida sem devedor', inplace=True)

def substitui_tipo():
    tabela[['PARCELA', 'TOTAL PARCELAS']] = tabela[['PARCELA', 'TOTAL PARCELAS']].values.astype(np.int64)

def cria_lista_total_parcelas():
    lista_total_parcelas = tabela['TOTAL PARCELAS'].tolist()
    return lista_total_parcelas

def cria_lista_parcela_atual():
    lista_parcela_atual = tabela['PARCELA'].tolist()
    return lista_parcela_atual

def cria_lista_parcelas_restantes():
    total_parcelas = cria_lista_total_parcelas()
    parcela_atual = cria_lista_parcela_atual()
    lista_parcelas_restantes = [elemen1 - elemen2 for elemen1, elemen2 in zip(total_parcelas, parcela_atual)]
    return lista_parcelas_restantes

def cria_lista_valor_parcelas():
    lista_valor_parcelas = tabela['VALOR A PAGAR'].tolist()
    return lista_valor_parcelas

def cria_lista_dividas():
    lista_dividas = tabela['DÍVIDAS'].tolist()
    return lista_dividas

def cria_lista_credores():
    lista_credores = tabela['CREDOR'].tolist()
    return lista_credores

def cria_lista_devedores():
    lista_devedores = tabela['DEVEDOR'].tolist()
    return lista_devedores

def cria_lista_total_debito():
    lista_valor_parcelas = cria_lista_valor_parcelas()
    lista_total_debito = lista_valor_parcelas
    return lista_total_debito

def dividas_cartao_credito():
    lista_credores = cria_lista_credores()
    lista_total_debito = cria_lista_total_debito()
    for i in lista_credores:
        if i == 'Crédito Nubank':
            lista_total_credito.append(lista_credores.index(i))
    for i in lista_total_credito:
        lista_total_debito.pop(i)
        i += 1
    return lista_total_debito

def mostra_total():
    lista_total_debito = dividas_cartao_credito()
    total_valor_devido = round(sum(tabela['VALOR A PAGAR']), 2)
    total_valor_recebido = round(sum(tabela['VALOR A RECEBER']), 2)
    total_valor_debito = round(sum(lista_total_debito), 2)
    print(f'\nTotal received {mes_atual}: R$ {total_valor_recebido}')
    print(f'Total debts {mes_atual}: R$ {total_valor_devido}')
    print(f'Total credit card debts {mes_atual}: R$ {total_valor_devido - total_valor_debito:.2f}')
    print(f'Total remaining in account {mes_atual}: R$ {total_valor_recebido - total_valor_debito:.2f}')

def menu_dividas(variavel, formatacao_texto='', cont=0, indice_menu=0, indice_lista=0):
    lista_dividas = cria_lista_dividas()
    print('Escolha uma das dívidas:')
    while cont < len(lista_dividas):
        print(f'({indice_menu}) - {lista_dividas[indice_lista]}')
        indice_menu += 1
        indice_lista += 1
        cont += 1
    print('(00) - Sair')
    escolha_dividas = int(input('> '))
    if escolha_dividas == 00:
        print('Encerrando programa...')
        exit()
    print(f'\n{lista_dividas[escolha_dividas]}\n{formatacao_texto} {variavel[escolha_dividas]}')

def menu(escolha_menu):
    lista_valor_parcelas = cria_lista_valor_parcelas()
    lista_parcelas_restantes = cria_lista_parcelas_restantes()
    lista_credores = cria_lista_credores()
    lista_devedores = cria_lista_devedores()
    lista_parcela_atual = cria_lista_parcela_atual()
    lista_total_parcelas = cria_lista_total_parcelas()
    while escolha_menu == 0:
        escolha_menu = int(input('\nEscolha uma opção:\n(1) - Valor da parcela?\n(2) - Quantas parcelas faltam?\n'
                                 '(3) - Quem é o credor da dívida?\n(4) - Quem é o devedor da dívida?\n'
                                 '(5) - Qual a parcela atual?\n(6) - Foi parcelado em quantas vezes?\n(7) - Sair\n> '))
        print('\n')
        if escolha_menu == 7:
            print('Encerrando programa...')
            break
        elif escolha_menu == 1:
            menu_dividas(lista_valor_parcelas, 'R$')
        elif escolha_menu == 2:
            menu_dividas(lista_parcelas_restantes, 'Parcelas restantes: ')
        elif escolha_menu == 3:
            menu_dividas(lista_credores, 'Pagar para: ')
        elif escolha_menu == 4:
            menu_dividas(lista_devedores, 'Receber de: ')
        elif escolha_menu == 5:
            menu_dividas(lista_parcela_atual, 'Parcela: ')
        elif escolha_menu == 6:
            menu_dividas(lista_total_parcelas, 'Total de parcelas: ')

substitui_valores()
substitui_tipo()
mostra_total()
menu(0)