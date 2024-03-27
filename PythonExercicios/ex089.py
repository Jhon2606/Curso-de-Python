lista = list()
lista2 = list()
lista3 = list()
lista4 = list()
continuar = ' '
count = 0
while True:
    lista.append(str(input('Nome: ').strip()))
    lista.append(int(input('Nota 1: ')))
    lista.append(int(input('Nota 2:')))
    lista2.append(lista[:])
    lista.clear()
    count +=1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).strip().upper()
    if continuar in 'N':
        break
    continuar = ' '
for i in range(0, len(lista2)):
    media = (lista2[i][1] + lista2[i][2]) / 2
    lista3.append(i)
    lista3.append(lista2[i][0])
    lista3.append(media)
    lista4.append(lista3[:])
    lista3.clear()
print('-=' * 25)
print('No.  Nome  Média')
for i in range(0, len(lista4)):
    print(f'{lista4[i]}')
aluno = int(input('Mostrar as notas de qual aluno? (999 para sair)'))
for c, i in enumerate(lista2):
    if aluno == 999:
        break
    if aluno == c:
        print(f'Notas de {lista2[c][0]} são [{lista2[c][1]}, {lista2[c][2]}]')