print('=' * 25) 
print('BANCO DO JHON') 
print('=' * 25)
val = int(input('Que valor você quer sacar? R$'))
total = val
ced = 50
count = 0
while True:
    if total >= ced:
        total -= ced
        count += 1
    else:
        if count > 0:
            print(f'Total de {count} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        count = 0
        if total == 0:
            break
print('=' * 25)
print('Volte sempre e tenha um bom dia!') 