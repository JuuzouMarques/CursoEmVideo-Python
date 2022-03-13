frase = input('Digite a frase: ')
frase = frase.replace(' ', '')
novaFrase = ''
for i in range(len(frase) - 1, -1, -1):
    novaFrase += frase[i]
print('A frase digitada {}é um palíndromo'.format('' if novaFrase == frase else 'não '))
