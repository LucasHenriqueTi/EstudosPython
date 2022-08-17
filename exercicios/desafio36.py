casa=float(input('Qual o valor da casa? '))
salário=float(input('Qual o seu salário? '))
anos=int(input('Em quantos anos você quer parcelar? '))
s1= casa/(anos*12)
s2= salário*0.30
print('Para pagar uma casa de R${:.3f} em {} anos a prestação será de R${:.2f}'.format(casa,anos,s1))
if s2>=s1:
    print('Empréstimo pode ser CONCEDIDO! ')
else:
    print('Empréstimo NEGADO')

