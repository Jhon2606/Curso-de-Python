n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
     'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 
     'dezenove', 'vinte')
n1 = 0
n2 = 'S'
while True:
    if n2 == 'S':
        n1 = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n1 <= 20:
            print(f'Você digitou o número {n[n1]}')
            n2 = ' '
        while n2 not in 'SN':
            n2 = str(input('Quer continuar? [S/N]')).strip().upper()
        if n1 < 0 or n1 > 20:
            print('Tente novamente.', end= ' ')
    else:
        break
