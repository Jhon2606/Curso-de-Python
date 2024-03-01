num = int(input('Digite um número:'))
count = 0
for prim in range(1, num + 1):
    if num % prim == 0:
        print('\033[33m', end=' ')
        count += 1
    else:
        print('\033[31m', end=' ')
    print(prim, end=' ')
if count >= 3:
    print('\n\033[mO número não é primo')
else:
    print('\n\033[mO número é primo')