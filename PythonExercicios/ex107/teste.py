import moeda
p = float(input('Digite um preço: R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentanto 10% temos {moeda.aumentar(p, 10)}')