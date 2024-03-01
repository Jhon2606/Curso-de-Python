frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
## inverso = junto[::-1] essa é oura forma de fazer
print('Você digitou a frase {}'.format(frase))
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')