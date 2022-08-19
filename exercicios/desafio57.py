""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto. """

#solução fazendo sozinho
'''sexo = str(input('Informe seu sexo: [M] para mascúlino ou [F] para feminino: ')).lower().strip()
if sexo == 'm':
    print('Sexo Masculino resgistrado com sucesso!')
elif sexo == 'f':
    print('Sexo Feminino registrado com sucesso!')
else:
    n1 = ''
    while n1 == '':
        sexo1 = str(input('DADOS INVALIDOS. POR FAVOR, INFORME SEU SEXO:  ')).lower().strip()
        if sexo1 == 'f':
            n1 = sexo1
            print('sexo Feminino registrado com sucesso!')
        elif sexo1 == 'm':
            n1 = sexo1
            print('sexo Masculino registrado com sucesso!')'''

#solução correta
sexo = str(input('Informe seu sexo: [M] para mascúlino ou [F] para feminino: ')).lower().strip()
while sexo not in 'f''m':
    sexo = str(input('DADOS INVALIDOS. POR FAVOR, INORME SEU SEXO: '))
print('sexo {} registrado com sucesso!'.format(sexo))
