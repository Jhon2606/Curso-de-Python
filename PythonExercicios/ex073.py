times = ('Atlético Mineiro', 'Vasco da Gama', 'Flamengo', 'Fluminense', 
         'Botafogo', 'Paranaense', 'Cuiaba Esporte Clube', 
         'Red Bull Bragantino', 'Corinthians', 'Internacional', 
         'Criciuma', 'Bahia', 'Goianiense', 'Fortaleza', 
         'Gremio Porto Alegrense', 'Palmeiras', 'Sao Paulo', 
         'Cruzeiro', 'Vitoria', 'Juventude')
print('-=-' * 50)
print(f'Lista de times do Brasileirão: {times}')
print('-=-' * 50)
print(f'Os cinco primeiros times são: {times[:5]}')
print('-=-' * 50)
print(f'Os quatro ultimos são: {times[-4:]}')
print('-=-' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 50)
print(f'O Flamengo está na posição {times.index('Flamengo')+1}')