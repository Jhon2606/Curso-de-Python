import math
a = float(input('Digite o cateto oposto:'))
b = float(input('Digite o cateto adjacente:'))
c = math.hypot(a, b)
print('A  Hipotenusa vale:{:.2f}'.format(c))