from random import shuffle

n1 = input('Digite o número do primeiro aluno: ')
n2 = input('Digite o número do segundo aluno: ')
n3 = input('Digite o número do terceiro aluno: ')
n4 = input('Digite o número do quarto aluno: ')
lista = [n1, n2, n3, n4]

print('A ordem de apresentação será: {}'.format(shuffle(lista)))