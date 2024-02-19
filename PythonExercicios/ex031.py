km = float(input('Quantos km você vai viajar?'))
if km <= 200:
    via = km * 0.50
    print('A sua viagem custará R${:.2f}'.format(via))
else:
    via = km * 0.45
    print('A sua viagem custará R${:.2f}'.format(via))