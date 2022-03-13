sum, c, maiorIdade = 0, 0, 0
maisVelho = ''
for i in range(4):
    idade = int(input('Idade: '))
    nome = input('Nome: ')
    sexo = input('Sexo (m/f): ')
    sum += idade
    if idade > maiorIdade and sexo == 'm':
        maiorIdade == idade
        maisVelho = nome
    if idade < 20 and sexo == 'f':
        c += 1
media = sum / 4
print('Média das idades: {}'.format(media))
print('Nome do homem mais velho: {}'.format(maisVelho))
print('Quantidade de mulheres com menos de 20: {}'.format(c))
