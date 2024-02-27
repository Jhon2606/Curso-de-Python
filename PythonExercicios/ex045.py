from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
jog = int(input('''Suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA
Qual é a sua jogada?'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-' * 15)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jog]))
print('-=-' * 15)

if comp == 0:
    if jog == 0:
        print('Empate!')
    elif jog == 1:
        print('Computador venceu!')
    elif jog == 2:
        print('Jogador Vence!')
    else:
        print('Jogada inválida!')
elif comp == 1:
    if jog == 0:
        print('Computador venceu!')
    elif jog == 1:
        print('Empate!')
    elif jog == 2:
        print('Jogador Vence!')
    else:
        print('Jogada inválida!')
elif comp == 2:
    if jog == 0:
        print('Jogador Vence!')
    elif jog == 1:
        print('Computador venceu!')
    elif jog == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')