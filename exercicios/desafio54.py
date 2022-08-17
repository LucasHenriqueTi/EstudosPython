from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade < 21:
        menor += +1
    else:
        maior += +1
print('ao todo tivemos {} pessoas maiores de idade!'.format(maior))
print('ao todo tivemos {} pessoas menores de idade!'.format(menor))
