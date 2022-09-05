"""Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""

aluno = {'nomes': str(input('Nome do aluno: '))}
aluno['média'] = int(input(f'média de {aluno["nomes"]}: '))
print(f'o nome do aluno é {aluno["nomes"]}')
print(f'a média dele é {aluno["média"]}')
if aluno['média'] > 7:
    print('Situação, APROVADO')
elif 5 <= aluno['média'] < 7:
    print('Stuação, RECUPERAÇÃO')
else:
    print('Situação, REPROVADO')
