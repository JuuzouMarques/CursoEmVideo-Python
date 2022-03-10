from datetime import date

dataAtual = int(date.today().strftime('%Y'))
idade = dataAtual - int(input('Digite a sua data de nascimento: '))
print('Sua categoria: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
