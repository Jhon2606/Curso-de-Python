print('=' * 20)
print('   10 Termos da PA')
print('=' * 20)
prim = int(input('Digite o primeiro termo:'))
raz = int(input('Digite a razão:'))
décimo = prim + (10 - 1) * raz
for num in range(prim, décimo + raz, raz):
    print(num, end= ' ==> ')
print('Acabou')