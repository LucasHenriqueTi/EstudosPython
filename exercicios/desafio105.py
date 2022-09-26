"""Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)"""


def notas(*n, sit=False):
    r = {'total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': sum(n) / len(n)}
    if sit:
        if r['Média'] >= 7:
            print('SITUAÇÃO BOA')
        else:
            print('SITUAÇÃO RUIM')
    return r


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
