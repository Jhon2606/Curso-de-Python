def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma(4, 5)
soma(b = 1, a = 2)
soma(3, 6)
print()
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
contador(2, 1, 0)
contador(7, 5, 9)
contador(3, 9, 6)
print()
def contador2(*num):
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números')
contador2(2, 1, 0)
contador2(7, 5, 9)
contador2(3, 9, 6)
print()
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [1, 2, 3, 4]
dobra(valores)
print(valores)
print()
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os {valores} temos {s}')
soma(5, 2)
soma(2, 9, 4)
print()