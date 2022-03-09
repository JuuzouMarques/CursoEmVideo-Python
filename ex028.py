from random import randint

escolhido = randint(0, 5)
numero = int(input('Digite um número entre 0 e 5: '))
print('Você acertou o número escolhido' if numero == escolhido else 'Errou, o número correto era {}'.format(escolhido))
