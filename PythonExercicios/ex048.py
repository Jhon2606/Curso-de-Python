som = 0
n = 0
for num in range(1, 500, 2):
    if num % 3 == 0:
        som += num
        n += 1
print('A soma de todos os {} valores solicitados é {}'.format(n, som))