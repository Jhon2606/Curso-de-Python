from random import randint
print('=-' * 25)
print('Vamos jogar par ou impar!')
print('=-' * 25)
c = venceu = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end= ' ')
        print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            venceu += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            venceu += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {venceu} vezes')