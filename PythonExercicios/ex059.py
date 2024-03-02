from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
cmd = 0
while cmd != 5:
    cmd = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Qual sua opção? '''))
    if cmd == 1:
        resp = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, resp))
    elif cmd == 2:
        resp = num1 * num2
        print('A multiplicação entre {} * {} é {}'.format(num1, num2, resp))
    elif cmd == 3:
        if num1 > num2:
            resp = num1
            print('Entre {} e {} a maior opção é {}'.format(num1, num2, resp))
        elif num2 > num1:
            resp = num2
            print('Entre {} e {} a maior opção é {}'.format(num1, num2, resp))
        else:
            print('Os números são iguais')
    elif cmd == 4:
        print('Informe os números novamente:')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif cmd == 5:
        print('Finlizando...')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 20)
    print('...')
    sleep(2)
print('Volte sempre!')