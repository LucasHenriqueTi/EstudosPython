aluno = {'nomes': str(input('Nome do aluno: '))}
aluno['média'] = int(input(f'média de {aluno["nomes"]}: '))
print(f'o nome do aluno é {aluno["nomes"]}')
print(f'a média dele é {aluno["média"]}')
if aluno['média'] > 6:
    print('Situação, APROVADO')
else:
    print('Situação, REPROVADO')
