from time import sleep
def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print(f'Contgem de {a} até {b} de {c} em {c}.')
    sleep(2.5)
    if a >= b:
        for i in range(a, b-c, -c):
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
    else:
        for i in range(a, b+1, c):
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
    print()
def linha():
    print('=-' * 20)
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contador(x, y, z)
linha()

##OU


