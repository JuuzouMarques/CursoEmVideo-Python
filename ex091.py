from random import randint
from time import sleep

jogadores = dict()
print('Valores sorteados:')
for i in range(1, 5):
    jogadores[f'{i}º'] = randint(1, 6)
    print(f'O jogador {i} tirou {jogadores[f"{i}º"]}')
    sleep(1)