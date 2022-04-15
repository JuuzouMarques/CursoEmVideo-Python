from lib.interface import *

# PROGRAMA PRINCIPAL
while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('OPÇÃO 1')
    elif resposta == 2:
        print('OPÇÃO 2')
    elif resposta == 3:
        print('Saindo do Sistema! Até logo!')
        break
    else:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')