from datetime import date

anoAtual = date.today().year
idade = anoAtual - int(input('Digite seu ano de nascimento: '))
if idade < 18:
    print('Você deve se alistar em {} anos.'.format(18 - idade))
elif idade > 18:
    print('Já passou {} anos de seu período de alistamento'.format(idade - 18))
else:
    print('Você está no ano de alistamento')
