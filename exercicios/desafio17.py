from math import hypot
n1= float(input('valor do cateto oposto: '))
n2= float(input('valor do cateto adjacente: '))
s1= hypot(n1,n2)
print('a valor da Hipotenusa é {:.2f}'.format(s1))
