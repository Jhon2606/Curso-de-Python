from datetime import date
ano = int(input('Digite seu ano de nascimento:'))
atual = date.today().year
ano2 = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, ano2, atual))
if ano2 < 18:
    saldo = 18 - ano2
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif ano2 > 18:
    saldo = ano2 - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Você deve se alistar imediatamente')