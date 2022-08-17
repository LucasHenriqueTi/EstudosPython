n1=int(input('1º valor: '))
n2=int(input('2º valor: '))
n3=int(input('3º valor: '))
s1=n1
if n2<n1 and n2<n3:
    s1=n2
if n3<n1 and n3<n2:
    s1=n3
print('o menor valor é {} '.format(s1))
s2=n1
if n2>n1 and n2>n3:
    s2=n2
if n3>n1 and n3>n2:
    s2=n3
print('o maior valor é {} '.format(s2))
