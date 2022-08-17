peso=float(input('Qual seu peso? '))
altura=float(input('Qual sua altura? '))
imc=peso/(altura**2)
print('seu IMC é de {:.0f}'.format(imc))
if imc<18.5:
    print('Você está Abaixo do Peso!')
elif imc<25:
    print('Você está no Peso Ideal!')
elif imc<30:
    print('Você está com Sobrepeso!')
elif imc<40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Morbida!')
