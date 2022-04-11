from operator import itemgetter
from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6),
            'jogador2': randint(1,6),
            'jogador3': randint(1,6),
            'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
