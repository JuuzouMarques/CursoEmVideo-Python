from random import randint

escolhido = randint(1, 11)
tentativas = 1
numero = int(input('Digite um número entre 1 e 10: '))
while numero != escolhido:
    numero = int(input('Você errou! Digite outro número: '))
    tentativas += 1
print('Você acertou o número escolhido em {} tentativas'.format(tentativas))
