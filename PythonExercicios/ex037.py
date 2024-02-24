num = int(input('Digite um número qualquer:'))
print('''[ 1 ] coverter para BINÁRIO
[ 2 ] coverter para OCTAL
[ 3 ] coverter para HEXADECIMAL''')
n = int(input('Sua opção:'))

if n == 1:
    print('{} covertido para binário é {}'.format(n, bin(num)[2:]))
elif n == 2:
    print('{} covertido para octal é {}'.format(n, oct(num)[2:]))
elif n == 3:
    print('{} covertido para hexadecimal é {}'.format(n, hex(num)[2:]))
else:
    print('\033[7;30;40mOpção inválida\033[m')