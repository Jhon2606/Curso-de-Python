print('\033[1;31;40mOlá mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Jhonatas'
print('Prazer em te conhecer {}{}{}'.format('\033[3;34m', nome, '\033[m'))

cores = { 'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Prazer em te conhecer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))