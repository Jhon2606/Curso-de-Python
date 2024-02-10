import math
n1 = float(input('Digite um angulo:'))
n2 = math.sin(math.radians(n1))
n3 = math.tan(math.radians(n1))
n4 = math.asin(math.radians(n1))
print('O seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}:'.format(n2, n3, n4))