import uteis as u


# PROGRAMA PRINCIPAL
u.verificaArquivo()
while True:
    u.mostraTitulo()
    escolha = input('Sua escolha: ')
    if escolha == '1':
        u.listarCadastros()
    elif escolha == '2':
        u.novoCadastro()
    elif escolha == '3':
        print('VOLTE SEMPRE!')
        break
    else:
        print('\033[1;31mERRO! Por favor, selecione uma opção válida!\033[m')