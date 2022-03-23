listagem = ('Queijo', 5.3, 'Pão', 0.5, 'Margarina', 2.5, 'Pavê', 0.6, 'Bolo de fubá', 250.99)

print('{0}\n{1:^40}\n{0}'.format('-' * 40, 'LISTAGEM DE PREÇOS'))
for i in range(0, len(listagem), 2):
    print('{:.<30}R$ {:3.2f}'.format(listagem[i], listagem[i + 1]))
print('-' * 40)
