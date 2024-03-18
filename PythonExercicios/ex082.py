lista = []
lista1 = []
lista2 = []
while True:
    lista.append(int(input('Digite um número: ')))
    c = str(input('Quer continuar? [S/N]')).strip().upper()
    if c in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista1.append(v)
    elif v % 2 == 1:
        lista2.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista1}')
print(f'A lista de ímpares é {lista2}')