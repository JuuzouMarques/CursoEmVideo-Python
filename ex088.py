from random import randint

qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))
mega = []
jogos = []
for i in range(qtdJogos):
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
        if len(jogos) >= 6: break
    jogos.sort()
    mega.append(jogos[:])
    jogos.clear()
for i, jogo in enumerate(mega):
    print(f'Jogo {i+1}: {jogo}')
