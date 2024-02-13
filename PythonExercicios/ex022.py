nome = str(input('Qual é o seu nome:')).strip()

print('Seu nome maiuscúlo é: {}'.format(nome.upper()))
print('Seu nome minúsculo é {}'.format(nome.lower()))

print('Seu nome tem: {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))