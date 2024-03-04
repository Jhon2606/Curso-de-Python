from time import sleep
n = int(input('Digite um número: '))
s = 'S'
c = 1
maior = n1 = 0
menor = n
while s == 'S':
    s = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if s == 'S':
            n1 += n
            if  n < menor:
                menor = n
            if n > maior:
                maior = n
            n  = int(input('Digite um número: '))
            c += 1
    elif s == 'N':
         print('Processando...')
         sleep(2)
    else:
         print('Inválido.')
media = n1 / c
print('Você digitou {} números e a média foi {:.2f}'.format(c, media))
print('O valor maior foi {} e o menor valor foi {}'.format(maior, menor))
