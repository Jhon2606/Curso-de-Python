from datetime import date
ano = date.today().year
count = 0
count1 = 0
for pessoa in range(1, 8):
    pessoa = int(input('Em que ano a {}ª pessoa nasceu?'.format(pessoa)))
    if (ano - pessoa) > 18:
        count += 1
    else:
        count1 += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade.'.format(count, count1))