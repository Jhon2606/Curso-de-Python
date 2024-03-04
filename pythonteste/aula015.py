n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

nome = 'José'
salario = 987.3
idade = 33
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')