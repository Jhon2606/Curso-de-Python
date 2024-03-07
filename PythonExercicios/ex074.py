from random import randint
n = randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)
print(f'Os valores sorteados foram: {n}')
print(f'O menor valor sorteado foi {max(n)}')
print(f'O maior valor sorteado foi {min(n)}')