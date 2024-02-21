print('-=-' * 20)
print('Jogando com retas')
print('-=-' * 20)

r1 = int(input('Digite o comprimento da primeira reta:'))
r2 = int(input('Digite o comprimento da segunda reta:'))
r3 = int(input('Digite o comprimento da terceira reta:'))

if (r1 + r2) < r3 and (r2 + r3) < r1 and (r3 + r1) < r2:
    print('As retas não formam um triângulo')
else:
    print('As retas formam um triângulo')