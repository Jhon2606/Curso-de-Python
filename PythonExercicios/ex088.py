from random import randint
from time import sleep
print('=-' * 25)
print('JOGA NA MEGA SENA')
print('=-' * 25)
mega = list()
count = 0
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(1, jogos + 1):
    while count < 6:
        num = randint(1, 61)
        if num not in mega:
            mega.append(num)
            count += 1
    mega.sort()
    sleep(1)
    print(f'Jogo {i}: {mega}')
    mega.clear()
    count = 0
print('BOA SORTE!')