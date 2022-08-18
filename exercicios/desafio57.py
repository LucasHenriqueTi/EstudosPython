n1 = ''
while n1 != 'f' or 'm':
    sexo = str(input('Qual o seu gênero? [M/F] '))
    if sexo == 'm' or 'f':
        n1 += sexo

print(n1)