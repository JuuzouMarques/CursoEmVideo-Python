import csv


arquivo = 'ex115\\teste.csv' # Diretório do arquivo com os cadastros
red     = '\033[1;31m'  # Cor vermelha
green   = '\033[1;32m'  # Cor verde
normal  = '\033[m'      # Cor padrão

def verificaArquivo():
    try:
        _ = open(arquivo, 'r')
        _.close()
    except:
        print('ARQUIVO NÃO ENCONTRADO')
        _ = open(arquivo, 'w')
        _.close()


def mostraTitulo():
    print('~' * 50)
    print('CADASTROS'.center(50))
    print('~' * 50)
    print('''Selecione a opção desejada:
    [ 1 ] Listar Pessoas Cadastradas
    [ 2 ] Cadastrar Nova Pessoa
    [ 3 ] Encerrar Programa''')


def listarCadastros():
    print('-' * 50)
    print(f'{"NOME":<40}{"IDADE":<10}')
    print('-' * 50)
    with open(arquivo) as arq:
        reader = csv.reader(arq)
        for row in reader:
            print(f'{row[0]:<40}{row[1]:<10}')
    # for cad in dados:
    #     print(f'{cad["nome"]:<40}{cad["idade"]:<10}')    
    print('-' * 50)


def novoCadastro():
    novo = list()
    print('-' * 50)
    while True:
        novo.clear()
        try:
            novo.append(input('Nome da pessoa: ').strip().title())
            novo.append(int(input('Idade da pessoa: ')))
        except:
            print(f'{red}ERRO NA ENTRADA DE DADOS! Por favor, tente novamente!{normal}')
        else:
            break
    try:
        with open(arquivo, 'w') as arq:
            csv.writer(arq, delimiter=',').writerow(novo)
    except:
        print(f'{red}ERRO NO CADASTRO DA PESSOA!{normal}')
    else:
        print(f'{green}CADASTRO EFETUADO COM SUCESSO!{normal}')
    print('-' * 50)


# PROGRAMA PRINCIPAL
dados = []
verificaArquivo()
while True:
    mostraTitulo()
    escolha = input('Sua escolha: ')
    if escolha == '1':
        listarCadastros()
    elif escolha == '2':
        novoCadastro()
    elif escolha == '3':
        print('VOLTE SEMPRE!')
        break
    else:
        print('\033[1;31mERRO! Por favor, selecione uma opção válida!\033[m')