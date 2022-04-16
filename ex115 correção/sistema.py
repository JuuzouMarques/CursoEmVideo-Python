from lib.interface import *
from lib.arquivo import *

arq = 'ex115 correção\\dados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

# PROGRAMA PRINCIPAL
while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema! Até logo!')
        break
    else:
        print('ERRO! Selecione uma opção válida!')
