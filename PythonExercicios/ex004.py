j = input('Digite algo:')
print(j,'é do tipo', type(j))
print('Tem letra e número?', j.isalnum()) #Letra e número
print('Tem apenas letras?', j.isalpha()) #Letra
print('É um caractere é do tipo 7-bit US-ASCII?', j.isascii()) #Verifica se um caractere é do tipo 7-bit US-ASCII
print('É um número entre 0 e 9?', j.isdigit()) #Checa se os caracteres de um string são números entre 0 e 9
print('Começa com letra minúscula?', j.islower()) #Verifique se todos os caracteres do texto estão em letras minúsculas
print('Todos os caracteres na string são decimais?', j.isdecimal()) #Retorna True se todos os caracteres em uma string forem decimais.
print('É um identificador válido?', j.isidentifier()) #Método retorna True se a string for um identificador válido, caso contrário, False.Uma string é considerada um identificador válido se contiver apenas letras alfanuméricas (az) e (0-9) ou sublinhados (_). Um identificador válido não pode começar com um número ou conter espaços.
print('É tudo número?', j.isnumeric()) #Verifica se todos os caracteres são numéricos ou não.
print('Da pra imprimir?', j.isprintable()) #Verifique se todos os caracteres do texto são imprimíveis
print('É um espaço em branco?', j.isspace()) #Verifica se todos os caracteres são de espaço em branco ou não
print('Todos os caracteres do texto estão em maiúsculas?', j.isupper()) #Verifique se todos os caracteres do texto estão em maiúsculas
print('Começa com uma letra maiúscula?', j.istitle()) #Verifique se cada palavra começa com uma letra maiúscula
