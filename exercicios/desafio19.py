from random import choice,shuffle
n1= input('digite o nome do 1º aluno: ')
n2= input('digite o nome do 2º aluno: ')
n3= input('digite o nome do 3º aluno: ')
n4= input('digite o nome do 4º aluno: ')
lista= [n1,n2,n3,n4]
s1= choice(lista)
print('o aluno escolhido para a apresentação foi {}'.format(s1))
