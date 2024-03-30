from datetime import date
sit = dict()
sit['Nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
sit['Idade'] = date.today().year - nasc
sit['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if sit['CTPS'] > 0:
    sit['Contratação'] = int(input('Ano de contratação: '))
    sit['Salário'] = float(input('Salário: R$'))
    sit['Aposentadoria'] = sit['Idade'] + ((sit['Contratação'] + 35) - date.today().year)
for i, v in sit.items():
    print(f'- {i} tem o valor {v}')