lanche = ('Haburguer', 'Suco',  'Pizza', 'Pudim')
#Tuplas são imutáveis
for c in lanche:
    print(f'Eu vou comer{c}')
for c in range(0, len(lanche)):
    print(lanche[c])
for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print(lanche)
print(sorted(lanche))
a = (2, 5, 4, 2)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(4))
print(c.index(8))
print(c.index(5, 2))
pessoa = ('Gustavo', 39,'M', 99.8)
print(pessoa)
del(pessoa)