n1 = count = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
        n1 += n
        count += 1
        n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma deles foi {}'.format(count, n1))
