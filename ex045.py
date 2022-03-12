from random import randint

while True:
    print('{}\nPEDRA, PAPEL, TESOURA\n{}'.format('-' * 20, '-' * 20))
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    print('''Escolha uma das opções
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA''')
    escolha = int(input('Sua escolha: ')) - 1
    if not escolha in [0, 1, 2]:
        break
    oponente = randint(0, 2)
    print('''VOCÊ JOGOU: {}
COMPUTADOR JOGOU: {}'''.format(opcoes[escolha], opcoes[oponente]))

    if oponente == escolha:
        print('EMPATE!')
    else:
        if oponente == 0:
            if escolha == 1:
                print('VITÓRIA!')
            else:
                print('DERROTA!')
        elif oponente == 1:
            if escolha == 0:
                print('DERROTA!')
            else:
                print('VITÓRIA!')
        else:
            if escolha == 0:
                print('VITÓRIA!')
            else:
                print('DERROTA!')
    print('')
