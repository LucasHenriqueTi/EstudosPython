from random import randint
jogos = int(input('quantos jogos você quer jogar? '))
for i, p in enumerate(range(0, jogos)):
    listap = []
    while True:
        num = randint(1, 60)
        if num not in listap:
            listap.append(num)
        if len(listap) == 6:
            break
    print(f'{i+1}º Jogo: {listap}')
    