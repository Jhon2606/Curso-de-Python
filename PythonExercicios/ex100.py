from random import randint
from time import sleep
def sorteia(num):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(1, 10)
        num.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')
numeros = list()
def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista} temos {soma}!')
sorteia(numeros)
somapar(numeros)