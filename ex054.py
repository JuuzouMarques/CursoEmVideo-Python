from datetime import date

c = 0
for i in range(7):
    ano = int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 10:
        c += 1
print('{} pessoas são de maioridade, e {} não'.format(c, 7 - c))
