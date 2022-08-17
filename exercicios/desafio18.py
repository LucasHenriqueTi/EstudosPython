from math import cos,tan,sin,radians
n1= int(input('digite um angulo: '))
s1= cos(radians(n1))
s2= tan(radians(n1))
s3= sin(radians(n1))
print('seno {:.2f}'.format(s3))
print('cosseno {:.2f}'.format(s1))
print('tangente {:.2f}'.format(s2))
