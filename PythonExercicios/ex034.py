sal = float(input('Digite o seu salário:'))
if sal <= 1250:
    sal = (sal * 0.15) + sal
else:
    sal = (sal * 0.10) + sal
print('Seu novo salário é de R${:.2f}'.format(sal))