num = []
posma = []
posme = []
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {n}:')))
print(f'Você digitou os valores {num}')
maior = num[0]
menor = num[0]
for n in range(0, len(num)):
    if num[n] > maior:
        maior = num[n]
    if num[n] < menor:
        menor = num[n]
for n, c in enumerate(num):
    if maior == num[n]:
        posma.append(n, )
    if menor == num[n]:
        posme.append(n, )
print(f'O maior valor digitado foi {maior} nas posições {posma}')
print(f'O menor valor digitado foi {menor} nas posições {posme}')