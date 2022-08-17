n1 = float(input('Qual o seu salário? '))
s1 = (n1*0.10)+n1 if n1>1250 else (n1*0.15)+n1
print('Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}'.format(n1,s1))
