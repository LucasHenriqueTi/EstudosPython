n1=float(input('digite o primeiro valor: '))
n2=float(input('digite o segundo  valor: '))
n3=float(input('digite o terceiro valor: '))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('os segmentos a cima pode sim ser um triângulo')
else:
    print('os segmentos a cima não pode ser um triângulo')