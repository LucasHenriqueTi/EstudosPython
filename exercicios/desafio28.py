from random import randint
from time import sleep
print('vou pensar em um número de 0 a 5, tente adivinhar qual...')
s1=randint(0,5)
n1=int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if s1==n1:
    print('Parabéns! Você conseguiu acertar o número')
else:
    print('Você Perdeu, eu pensei no número {} e não no {}'.format(s1,n1))
