def leiaInt(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            break
        print('ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!')
    return n


# Programa Principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')
