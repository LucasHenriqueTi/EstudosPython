from random import shuffle
n1= input('1º aluno: ')
n2= input('2º aluno: ')
n3= input('3º aluno: ')
n4= input('4º aluno: ')
lista= [n1,n2,n3,n4]
shuffle(lista)
print('a ordem de apresentação dos alunos são {}'.format(lista))