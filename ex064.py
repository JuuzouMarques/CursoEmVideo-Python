numero = 0
qtd = -1
sum = -999
while numero != 999:
    numero = int(input('Digite um número: '))
    sum += numero
    qtd += 1
print('Foram digitados {} números'.format(qtd))
print('O somatório de todos os números digitados foi {}'.format(sum))