lista = []
for i in range(3):
    lista.append(int(input('Digite um número: ')))

lista.sort()
print('O menor e o maior número são, respectivamente {} e {}'.format(lista[0], lista[2]))
