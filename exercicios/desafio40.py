n1=float(input('nota 1: '))
n2=float(input('nota 2: '))
s1= (n1+n2)/2
if s1<5:
    print('Suas notas foram muito baixa, você esta REPROVADO!!')
elif s1>=7:
    print('Suas notas foram exelentes, PAROVADO!! ')
else:
    print('Suas notas não foram tão boas, você esta de RECUPERAÇÃO!!')
