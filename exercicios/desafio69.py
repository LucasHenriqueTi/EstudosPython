"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:"""
idade = homens = mulheres = anos = 0
while True:
    anos = int(input('Qual sua Idade: '))
    sexo = pergunta = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if anos >= 18:
        idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and anos < 20:
        mulheres += 1
    if pergunta == 'N':
        break
print(f'{idade} pessoas tem mais de 18 anos.')
print(f'{homens} Homem(s) foram cadastrados.')
print(f'{mulheres} Mulher(es) tem menos de 20 anos')
