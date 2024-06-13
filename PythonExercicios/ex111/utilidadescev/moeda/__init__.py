def metade(preco = 0, formato = False):
    res = preco/2
    return res if formato is False else moeda(res)
def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)
def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(res)
def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)
def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')
def resumo(p = 0, taxa1 = 10, taxa2 = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço anlisado: \t{moeda(p)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(p, taxa1, True)}')
    print(f'{taxa2}% de aumento: \t{diminuir(p, taxa2, True)}')
    print('-' * 35)