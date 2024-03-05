print('-' * 25)
print('LOJA DO JHON')
print('-' * 25)
compra =  count = maismil = 0
produto = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: '))
    count += 1
    compra += preco
    if preco > 1000:
        maismil += 1
    if count == 1 or preco < maisbarato:
        maisbarato = preco
        produto = nome
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if c in 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA')) 
print(f'O total da compra foi R${compra:.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${maisbarato}')