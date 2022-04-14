def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!')
        else:
            break
    return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt).replace(',', '.'))
        except:
            print('ERRO! DIGITE UM NÚMERO VÁLIDO!')
        else:
            break
    return n


# Programa Principal
n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número decimal: ')
print(f'Você acabou de digitar os números {n} e {f}')
