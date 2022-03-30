from random import randint

qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))
mega = []
jogos = []
for i in range(qtdJogos):
    for j in range(6):
        jogos.append(randint(1, 60))
    mega.append(jogos[:])
    jogos.clear()
for i, jogo in enumerate(mega):
    print(f'Jogo {i+1}: {jogo}')
