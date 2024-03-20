lista = list()
dados = list()
maiorp = menorp = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Peso: ')))
    if len(dados) == 0:
        maiorp = menorp = lista[1]
    else:
        if lista[1] > maiorp:
            maiorp = lista[1]
        if lista[1] < menorp:   
            menorp = lista[1]
    dados.append(lista[:])
    lista.clear()
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(f'Ao todo você cadastrou {len(dados)} pessoas')
print(f'O maior peso foi de {maiorp}Kg. Peso de ', end= '')
for p in dados:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorp}Kg. Peso de ', end= '')
for p in dados:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='')
print()