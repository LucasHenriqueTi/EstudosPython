maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso ligo foi de {} Kg'.format(maior))
print('o menor peso ligo foi de {} Kg'.format(menor))

'''maior = 0
menor = float('inf')
for i in range(5):
    p = float(input('Peso: '))
    if p>maior:
        maior = p
    if p<menor:
        menor = p
print(f'Dentre esses, o maior peso foi {maior}kg e o menor foi {menor}kg ')'''
