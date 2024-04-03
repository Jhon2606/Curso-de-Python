tabela = dict()
gols = list()
galera = list()
cont = ''
while True:
    tabela.clear()
    gols.clear()
    tabela['jogador'] = str(input('Nome do jogador: ')).strip()
    val = int(input(f'Quantas partidas {tabela['jogador']} jogou? '))
    for i in range(0, val):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    tabela['gols'] = gols[:]
    tabela['total'] = sum(gols)
    galera.append(tabela.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if cont == 'N':
        break
print('=-' * 25)
print('cod          ', end='')
for i in tabela.keys():
    print(f'{i:<15}', end='')
print()
print('-----' * 10)
for i, j in enumerate(galera):
    print(f'{i:>3}', end=' ')
    for d in j.values():
        print(f'{str(d):>15}', end='')
    print()
print('-----' * 10)
while True:
    val = int(input('Mostrar dados que qual jogador? (999 para parar) '))
    if val == 999:
        break
    if val >= len(galera):
        print(f'ERRO! Não existe jogador com código {val}')
    else:
        print(f'LEVANTAMENTO DE DADOS DO JOGADOR {galera[val]["jogador"]}')
        for p, g in enumerate(galera[val]['gols']):
            print(f'     No jogo {p+1} fez {g} gols.')
    print('----' * 20)