from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar
print('-=-' * 20)
print('Estou pensando em um número...')
print('-=-' * 20)
jogador = int(input('Qual número eu pensei?')) #Jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Voce acertou eu pensei no {}'.format(jogador))
else:
    print('Você errou eu não pensei no {} eu pensei no {}'.format(jogador, computador))