num = [1, 2, 3, 4]
num[2] = 5
num.append(7)
num.sort()
num.sort(reverse= True)
num.insert(0, 9)
num.pop(2)
if 20 in num:
    num.remove(20)
else:
    print('Não achei o número 20')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(7)
valores.append(8)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [0, 3, 5, 9]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')