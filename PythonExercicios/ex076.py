lista = ('Lápis', 1.00, 'Caneta', 2.00, 'Caderno', 25.00, 'Borracha', 5.00, 'Estojo', 8.00)
print('-=' * 25)
print('Papelaria do Jhon')
print('-=' * 25)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>6.2f}')
print('-=' * 25)