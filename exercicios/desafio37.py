n1=int(input('Digite um número inteiro: '))
print('''Escolha uma das opções a baixo:
[1] converter para Binario
[2] converter para Octal
[3] converter para Hexadecimal''')
opção=int(input('Qual opção?'))
if opção == 1:
    print('O número {} convertido para Binário fica {}'.format(n1,bin(n1)[2:]))
elif opção == 2:
    print('O número {} convertido para Octal fica {}'.format(n1,oct(n1)[2:]))
elif opção == 3:
    print('O número {} convertido para Hexadecimal fica {}'.format(n1,hex(n1)[2:]))
else:
    print('OPÇÃO INVALIDA')
