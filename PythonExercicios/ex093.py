jog = dict()
golsl = list()
jog['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jog['jogador']} jogou? '))
for i in range(1, partidas+1):
    golsl.append(int(input(f'uantos gols na partida {i}? ')))
    jog['gols'] = golsl[:]
    jog['total'] = sum(golsl)
print('=-' * 25)
print(jog)
for i, v in jog.items():
    print(f'O campo {i} tem valor {v}')
print('=-' * 25)
print(f'O jogador {jog["jogador"]} jogou {partidas} partidas.')
for i, v in enumerate(jog['gols']):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols')