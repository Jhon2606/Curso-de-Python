from time import sleep
def maior(*num):
    print('=-' * 20)
    ma = 0
    for i in range(0, len(num)):
        if i == 0:
            ma = num[i]
        if num[i] > ma:
            ma = num[i]
    print('Analisando os valores passados...')
    for i in range(0, len(num)):
        print(f'{num[i]}', end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {ma}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()