def area(a, b):
    s = a * b
    print(f'A ária de um terreno {a}x{b} é de {s}m²')
print('CONTROLE DE TERRENOS')
print('-' * 20)
area(float(input('LARGURA (m): ')),
     float(input('COMPRIMENTO (m): ')))