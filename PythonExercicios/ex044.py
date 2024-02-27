val = float(input('Digite o preço:'))
print('Formas de pagamento:\n[1] à vista dinheiro cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
pag = int(input('Qual opção?'))

if pag == 1:
    val2 = val - (val * 0.10)
    print('A vista você recebe um deconto de 10%, sua compra de R${:.2f} sairá por R${:.2f}'.format(val, val2))
elif pag == 2:
    val2 = val - (val * 0.05)
    print('Sua compra de R${:.2f} com desconto de 5%, sairá por R${:.2f} a vista no cartão'.format(val, val2))
elif pag == 3:
    print('Sua compra dividida em 2x no cartão sairá por R${:.2f} ao final do pagamento'.format(val))
elif pag == 4:
    par = int(input('Quantas parcelas?'))
    if par == 1:
        val2 = val - (val * 0.05)
        print('Sua compra de R${:.2f} com desconto de 5%, sairá por R${:.2f} a vista no cartão'.format(val, val2))
    elif par == 2:
        print('Sua compra dividida em 2x no cartão sairá por R${:.2f} ao final do pagamento'.format(val))
    elif par >= 3:
        val2 = val + (val * 0.20)
        print('Sua compra de R${:.2f} parcelada em {}x ao final custará R${:.2f} com juros de 20%'.format(val, par, val2))
    else:
        print('Número inválido')
else:
    print('Opação inválida')