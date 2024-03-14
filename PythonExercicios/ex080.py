lista = []
for c in range(0, 5):
    val = int(input('Digite um valor: '))
    if c == 0 or val > lista[-1]:
        lista.append(val)
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos, val)
                break
            pos +=1
print(f'Os valores digitados foram {lista}')