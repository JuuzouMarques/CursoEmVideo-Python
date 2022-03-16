valor = 0
while valor != 5:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    valor = 0

    while not (valor == 4 or valor == 5):
        print('OPÇÕES')
        print('[1] SOMAR')
        print('[2] MULTIPLICAR')
        print('[3] MAIOR')
        print('[4] NOVOS NÚMEROS')
        print('[5] SAIR DO PROGRAMA')
        valor = int(input('Sua escolha: '))

        if valor == 1:
            print('\nA soma entre {} e {} resulta em {}\n'.format(num1, num2, (num1 + num2)))
        elif valor == 2:
            print('\nO produto entre {} e {} resulta em {}\n'.format(num1, num2, (num1 * num2)))
        elif valor == 3:
            if num1 > num2:
                print('\n{} é maior que {}\n'.format(num1, num2))
            elif num2 > num1:
                print('\n{} é maior que {}\n'.format(num2, num1))
            else:
                print('\nOs dois valores são iguais a {}\n'.format(num1))