"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
 por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date
catastro = {'nome': str(input('Nome: ')),
            'idade': date.today().year-int(input('Ano de Nascimento: ')),
            'ctlps': int(input('Carteira de Trabalho: [0 não tem] ')),
            }
if catastro['ctlps'] > 0:
    catastro['contratação'] = int(input('Ano de Contratação: '))
    catastro['salario'] = float(input('Sálario: R$'))
    print(f'Nome: {catastro["nome"]}')
    print(f'Idade: {catastro["idade"]}')
    print(f'Carteira de Trabalho: {catastro["ctlps"]}')
    print(f'Contratação: {catastro["contratação"]}')
    print(f'Sálario: {catastro["salario"]}')
    print(f'Se aposentara com {catastro["idade"] - ((date.today().year-catastro["contratação"]) - 35)}')
else:
    print(f'Nome: {catastro["nome"]}')
    print(f'Idade: {catastro["idade"]}')
    print(f'Carteira de Trabalho: {catastro["ctlps"]}')
