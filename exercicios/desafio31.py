'''n1= float(input('de quantos Km é sua viagem? '))
s1= n1*0.50
s2= n1*0.45
print('Você está prestes a começar uma viajem de {}Km'.format(n1))
if n1<=200:
    print('E o preço da sua passagem será de R${:.2f}'.format(s1))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(s2))'''

n1=float(input('de quantos Km é a sua viagem? '))
print('sua viagem é de {}Km'.format(n1))
s1= n1*0.50 if n1<=200 else n1*0.45
print('o preço da sua passagem será de R${:.2f}'.format(s1))
