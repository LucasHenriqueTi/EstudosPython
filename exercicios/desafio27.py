n1= str(input('digite seu nome completo: ')).strip().lower()
s1= n1.split()
print('seu primeiro nome é: {}'.format(s1[0]))
print('seu ultimo nome é {}'.format(s1[len(s1)-1]))