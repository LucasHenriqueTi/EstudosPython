from datetime import date
sexo=int(input('''Escolha uma das opções abaixo:
[1] HOMEM
[2] MULHER
Qual sua opção: '''))
if sexo==1:
    ano = int(input('qual seu ano de nascimento? '))
    atual = date.today().year
    idade = atual - ano
    atraso = idade - 18
    faltam = 18 - idade
    alistamento = atual - atraso
    alistamento1 = atual + faltam
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    if idade > 18:
        print('Você já deveria ter se alistado a {} anos! '.format(atraso))
        print('Seu alistamento foi em {}'.format(alistamento))
    elif idade < 18:
        print('Ainda faltam {} anos para o seu alistamento'.format(faltam))
        print('Seu alistamento é em {}'.format(alistamento1))
    elif idade == 18:
        print('Você precisa se alistar IMEDIATAMENTE')
elif sexo==2:
    print('O alistamento não é obrigatorio para mulheres!!')
    escolha=str(input('''Mesmo assim, Quer ver o seu alistamen?
Aperte [S] para SIM e [N] para NÃO: ''')).upper()
    if escolha=='S':
        ano = int(input('qual seu ano de nascimento? '))
        atual = date.today().year
        idade = atual - ano
        atraso = idade - 18
        faltam = 18 - idade
        alistamento = atual - atraso
        alistamento1 = atual + faltam
        print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
        if idade > 18:
            print('Você já deveria ter se alistado a {} anos! '.format(atraso))
            print('Seu alistamento foi em {}'.format(alistamento))
        elif idade < 18:
            print('Ainda faltam {} anos para o seu alistamento'.format(faltam))
            print('Seu alistamento é em {}'.format(alistamento1))
        elif idade == 18:
            print('Você precisa se alistar IMEDIATAMENTE')
    else:
        print('Ok, tenha um bom dia!!')
