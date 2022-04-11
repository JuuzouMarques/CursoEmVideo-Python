jogadores = list()
jogador = dict()
while True:
    jogador['nome'] = input('Nome: ')
    jogador['partidas'] = int(input('Quantidade de partidas: '))
    jogador['gols'] = []
    for i in range(jogador['partidas']):
        jogador['gols'].append(int(input(f'Gols na {i+1}ª partida: ')))
    jogador['totalGols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    jogador.clear()
    resposta = input('Deseja continuar [S/N]? ').strip().upper()[0]
    print('-' * 30)
    if resposta == 'N':
        break
print('-=' * 30)
print(f'cod {"nome":<15} {"gols":<15} total')
print('-' * 40)
for i, j in enumerate(jogadores):
    # print(f'{i} {j["nome"]} {j["gols"]} {j["totalGols"]}')
    print(f'{str(i):>3} {str(j["nome"]):<15} {str(j["gols"]):<15} {str(j["totalGols"])}')
print('-' * 40)
while True:
    resposta = int(input('Mostrar dados de qual jogador? '))
    if resposta == 999:
        break
    if resposta >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {resposta}. Tente novamente!')
    else:
        print(f'Levantamento do jogador {jogadores[resposta]["nome"]}:')
        for i in range(jogadores[resposta]['partidas']):
            print(f'No jogo {i+1} fez {jogadores[resposta]["gols"][i]} gols')
    print('-' * 30)
