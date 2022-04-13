def pyHelp(ajuda):
    s = f'     Acessando o comando\'{ajuda}\'     '
    print('~' * len(s))
    print(s)
    print('~' * len(s))
    print(help(ajuda))

# Programa Principal
while True:
    print('~' * 50)
    print(f'{"SISTEMA DE AJUDA PyHELP":^50}')
    print('~' * 50)
    ajuda = input('Função ou Biblioteca > ')
    if ajuda == 'FIM': break
    pyHelp(ajuda)
