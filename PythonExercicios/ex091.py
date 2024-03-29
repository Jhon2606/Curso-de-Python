from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = {}
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
ranking = dict()
print('Valores sorteados: ')
for i, v in jogadores.items():
    print(f'{i} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key= itemgetter(1), reverse= True)
print('=-' * 25)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
