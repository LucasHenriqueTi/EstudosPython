n1= int(input('digite um ano: '))
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('o ano {} é BISSEXTO'.format(n1))
else:
    print('O ano {} não é BISSEXTO'.format(n1))
    