preço=float(input('Valor da Compra: R$ '))
print('''Escolha uma das formas de pagamento a baixo:
[1] Dinheiro/Pix
[2] Cartão A Vista
[3] 2x no Crédito
[4] 3x ou mais no Crédito''')
fpagamento=int(input('Qual Opção você escolheu? '))
if fpagamento<=0 or fpagamento>4:
    print('Opção Invalida, Escolha Novamente')
if fpagamento==1:
    pix=preço-preço*0.10
    print('Com 10% de desconto sua compra fica R${:.2f}'.format(pix))
if fpagamento==2:
    avista=preço-preço*0.05
    print('Com 5% de desconto sua compra fica R${:.2f}'.format(avista))
if fpagamento==3:
    print('Seu produto em 2x no cartão de crédito fica R${:.2f}'.format(preço))
if fpagamento==4:
    cartão=preço+preço*0.20
    parcelas=int(input('Quantidade de parcelas: '))
    juros=cartão/parcelas
    print('Parcelando em 3x ou mais no credito, tem juros de 20%, o valor da sua compra fica R${:.2f} '.format(cartão))
    print('com parcelas de R${:.2f}'.format(juros))
