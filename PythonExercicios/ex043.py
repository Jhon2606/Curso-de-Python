peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))

imc = peso / (altura ** 2)
print('Com {:.1f}kg e {:.2f} de altura o seu IMC é de {:.1f} você está com '.format(peso, altura, imc), end='')

if imc < 18.5:
    print('peso abaixo do ideal.')
elif 18.5 <= imc < 25:
    print(' o peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
elif imc >= 40:
    print('obesidade mórbida')