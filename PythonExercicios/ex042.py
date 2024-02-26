print('-=-' * 20)
print('Jogando com retas')
print('-=-' * 20)

r1 = int(input('Digite o comprimento da primeira reta:'))
r2 = int(input('Digite o comprimento da segunda reta:'))
r3 = int(input('Digite o comprimento da terceira reta:'))

if (r2 + r3) > r1 and (r1 + r3) > r2 and (r2 + r1) > r3:
    print('As retas formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r3 == r2 or r3 == r1:
        print('ISÓCELES')
    else:
        print('ESCALENO')
else:
    print('As retas não formam um triângulo')