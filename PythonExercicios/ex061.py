print('Gerador de PA')
print('=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    print('{} '.format(p), end= '--> ')
    p += r
    c += 1
print('FIM')
