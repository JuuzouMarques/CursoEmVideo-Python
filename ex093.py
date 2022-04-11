jogador = dict()
jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input('Quantidade de partidas: '))
jogador['gols'] = []
for i in range(jogador['partidas']):
    jogador['gols'].append(int(input(f'Gols na {i+1}ª partida:')))
jogador['totalGols'] = sum(jogador['gols'])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for i in range(jogador['partidas']):
    print(f'    => Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["totalGols"]} gols')
