media = 0
maisvelho = 0
nome2 = ''
maisnova = 0
for grupo in range(1, 5):
    print('------ {}ª PESSOA ------'.format(grupo))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    if grupo == 1 and sexo in 'Mm':
         maisvelho = idade
         nome2 = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nome2 = nome
    if sexo in 'Ff' and idade < 20:
            maisnova += 1
    media += idade
media2 = media / 4
print('A média de idade do grupo é de {:.1f} anos'.format(media2))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelho, nome2))
print('Ao todo são {} mulheres com menos de 20 anos'.format(maisnova))