v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
if v1 > v2:
    print('\033[4;30;45mO primeiro valor é maior\033[m')
elif v2 > v1:
    print('\033[4;30;42mO segundo valor é maior\033[m')
else:
    print('Os dois valores são iguais')