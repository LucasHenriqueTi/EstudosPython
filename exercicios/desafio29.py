n1=float(input('qual a velocidade do seu carro? '))
s1=(n1-80)*7
print("Tenha um bom dia! Dirija com segurança!")
if n1>80:
    print('MULTADO, Você excedeu o limite permitido que é de 80Km/h Você deve pagar uma Multa de R${:.2f}!'.format(s1))