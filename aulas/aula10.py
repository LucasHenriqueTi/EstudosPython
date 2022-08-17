'''n1=int(input('quantos anos seu carro tem? '))
if n1<=3:
    print('seu carro é novo')
else:
    print('seu carro é velho')
print('fim')'''

'''simplicado
n1=int(input('quantos anos seu carro tem? '))
print('carro novo'if n1<=3 else 'carro velho')
print('FIM')'''

'''condição simples
n1=str(input('digite seu nome: '))
if n1=='lucas':
    print('que lindo nome!')
print('boa tarde, {}!'.format(n1))'''

'''condição composta
n1=str(input('Digite seu nome: '))
if n1=='lucas':
    print('Que nome Lindo!!')
else:
    print('seu nome é muito comum!!')
print('Bom Dia, {}!!'.format(n1))'''

n1= float(input('digite sua primeira nota: '))
n2= float(input('digite sua segunda nota: '))
n3= float(input('digite sua terceira nota: '))
s1= (n1+n2+n3)/3
print('sua média foi {:.1f}'.format(s1))
if s1>=6:
    print('PARABENS, você passou de ano!!')
else:
    print('Desculpe, Você está em recuperação, estude mais da proxima vez!!')
