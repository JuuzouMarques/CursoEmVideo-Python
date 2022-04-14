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
    for cad in dados:
        print(f'{cad["nome"]:<40}{cad["idade"]:<10}')    
    print('-' * 50)


def novoCadastro():
    novo = dict()
    print('-' * 50)
    nome = input('Digite um nome: ').strip().title()
    idade = int(input('Digite a idade: '))
    novo['nome'] = nome
    novo['idade'] = idade
    dados.append(novo)
    print('\033[1;32mCADASTRO EFETUADO COM SUCESSO!\033[m')
    print('-' * 50)


# PROGRAMA PRINCIPAL
dados = []
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
