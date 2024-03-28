aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['média'] = float(input('Média: '))
if aluno['média'] <= 5:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
     aluno['situação'] = 'Aprovado'
print('-=' * 25)
for i, v in aluno.items():
    print(f'- {i} é igual a {v}')