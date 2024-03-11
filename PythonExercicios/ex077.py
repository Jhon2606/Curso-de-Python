palavra = ('arroz', 'batata', 'feijao')
for c in palavra:
    print(f'\nNa palavra {c} temos: ', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')