nota = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))

media = (nota + nota2)/ 2
print('Tirando {:.1f} e {:.1f} sua nota será {:.1f}'.format(nota, nota2, media))

if media >= 7:
    print('APROVADO')
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')