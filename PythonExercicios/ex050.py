num1 = 0
cont = 0
for num in range(1, 7):
    num = int(input('Digite o {} valor:'.format(num)))
    if num % 2 == 0:
        num1 += num
        cont += 1
print('A soma dos {} números pares da lista é {}'.format(cont, num1))
