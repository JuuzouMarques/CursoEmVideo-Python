def ficha(nome, gols):
    if nome == '': nome = '<desconhecido>'
    if gols == '': gols = 0
    return f'O jogador {nome} fez {gols} gols no compeonato.'


# Programa Principal
jogador = input('Nome do jogador: ')
qtdGols = input('Quantidade de gols: ')
print(ficha(jogador, qtdGols))
