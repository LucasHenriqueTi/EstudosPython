"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""
listap = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    listap.append([nome, [nota1, nota2], (nota1+nota2)/2])
    sair = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
for i, p in enumerate(listap):
    print(f'{i} {p[0]:20} {p[2]}')
while True:
    perg = int(input('mostra as notas de qual aluno? (999 para interromper): '))
    if perg <= len(listap)-1:
        print(f'Notas de {listap[perg][0]} foram {listap[perg][1]}')
    if perg == 999:
        break
