vel = float(input('Digite a velocidade do carro:'))
if vel > 80:
    reais = (vel - 80) * 7 
    print('Você está acima do limite de velocidade, será multado em {:.2f} reais'.format(reais))
print('Tenha um bom dia e dirija com segurança!')