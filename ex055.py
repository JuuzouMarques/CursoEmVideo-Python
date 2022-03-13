lista = []
for i in range(5):
    peso = ('Peso da {}ª pessoa: '.format(i + 1))
    lista.append(peso)
lista.sort()
print('Menor peso: {}\nMaior peso: {}'.format(lista[0], lista[4]))
