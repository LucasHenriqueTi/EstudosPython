""" Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""


def voto(anos):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - anos
    if idade < 18:
        return f'{idade} anos Voto NEGADO'
    elif 18 <= idade < 64:
        return f'{idade} anos voto OBRIGATORIO'
    elif idade > 64:
        return f'{idade} anos voto OPCIONAL'


voto(1998)
