while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab * c}')
    print('-' * 35)
print('Programa de tabuada encerrado, volte sempre!')