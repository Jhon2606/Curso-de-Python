val = float(input('Digite o valor da casa:'))
sal = float(input('Digite o seu salário:'))
ano = int(input('Digite em quantos anos pretende pagar a casa:'))

prest = val / (ano * 12)
trintsal = 30 / 100 * sal
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(val, ano, prest))

if prest >= trintsal:
    print('\033[7;30;40mEmpréstimo negado!\033[m')
else:
    print('\033[7;33;46mEmpréstimo aceito!\033[m')