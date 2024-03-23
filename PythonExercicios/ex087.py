lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maiorval = somacolu = 0
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = int(input(f'Digite o valor [{i}, {j}]: '))
        if lista[i][j] % 2 == 0:
            somapar += lista[i][j]
        if j == 2:
            somacolu += lista[i][j]
        if i == 1:
            if lista[i][j] > maiorval:
                maiorval = lista[i][j]
print('=-' * 25)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^5}]', end='')
    print()
print(f'A soma dos valores pares é de {somapar}')
print(f'A soma dos valores da terceira coluna é de {somacolu}')
print(f"O maior valor da segunda linha é {maiorval}")