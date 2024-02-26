from datetime import date
idade = int(input('Digite o ano de nascimento:'))
ano = date.today().year
idade2 = ano - idade
print('O atleta tem {} anos'.format(idade2))

if 1 <= idade2 <= 9:
    print('Classificação: MIRIM')
elif idade2 <= 14:
    print('Classificação: INFANTIL')
elif idade2 <= 19:
    print('Classificação: JUNIOR')
elif idade2 <= 25:
    print('Classificação: SÊNIOR')
elif idade2 > 25:
    print('Classificação: MASTER')