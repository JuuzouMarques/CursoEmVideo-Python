from random import randint

c = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('=-' * 15)
    valor = int(input('Diga um valor: '))
    parImpar = input(('Par ou Ímpar? [P/I] '))[0].upper()
    computador = randint(0, 10)
    print('-' * 30)
    print(f'Você jogou {valor} e o computador {computador}. Total deu {valor + computador}')
    if (valor + computador) % 2 == 0:
        print(f'Deu PAR')
        if parImpar == 'I':
            break
    else:
        print(f'Deu IMPAR')
        if parImpar == 'P':
            break
    c += 1
    print('-' * 30)
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
print('Você PERDEU!')
print('=-' * 15)
print(f'Game Over! Você venceu {c} vezes')
