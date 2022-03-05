from random import shuffle

lista = []
for i in range(1, 5):
    aluno = input('Digite o nome do {}° aluno: '.format(i))
    lista.append(aluno)

shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
