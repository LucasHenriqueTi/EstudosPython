from datetime import date
anos=int(input('Seu ano de Nascimento: '))
anoatual=date.today().year
idade=anoatual-anos
if idade<=9 and idade>1:
    print('Você tem {} anos. Sua Categoria de Natação é MIRIM!'.format(idade))
elif idade>9 and idade<=14:
    print('Você tem {} anos. Sua Categoria de Natação é INFANTIL!'.format(idade))
elif idade>14 and idade<=19:
    print('Você tem {} anos. Sua Categoria de Natação é JUNIOR!'.format(idade))
elif idade>19 and idade<=20:
    print('Você tem {} anos. Sua Categoria de Natação é SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos. Sua Categoria de Natação é MASTER!'.format(idade))
    