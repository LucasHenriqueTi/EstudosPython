"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

sair = False
cont = total = menor = maior = 0
while not sair:
    num = int(input('digite um número: '))
    cont += 1
    total += num
    pergunta = str(input('Quer Continuar? [S/N]: ')).upper()
    if pergunta == 'N':
        sair = True
        print('Você digitou {} números e a media entre eles é {:.2f}'.format(cont, total/cont))
    if num == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
print('O maior numero digitado foi {} e o menor número digitado foi {}'.format(maior, menor))

