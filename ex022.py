nome = input('Digite seu nome completo: ')

print('Maisúculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Quantas letras: {}'.format(len(nome.replace(' ', ''))))
print('Letras no primeiro nome: {}'.format(len(nome.split()[0])))
