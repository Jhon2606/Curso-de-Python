val = []
while True:
  val2 = int(input('Digite um valor: '))
  if val2 not in val:
    val.append(val2)
    print('Valor adicionado com sucesso...')
  else:
    print('Valor duplicado! Não vou adicionar...')
  ver = str(input('Quer continuar? [S/N]')).strip().upper()
  if ver in 'N':
    break
val.sort()
print(f'Você digitou os valores {val}')