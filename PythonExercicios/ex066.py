c = s = 0
while True:
   v = int(input('Digite um valor [999 para parar]: '))
   if v == 999:
      break
   s += v
   c += 1
print(f'A soma dos {c} valores foi {s}')