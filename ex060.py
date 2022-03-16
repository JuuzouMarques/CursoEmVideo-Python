numero = int(input('Digite um número: '))
fatorial = numero
controle = numero - 1
while controle > 1:
    fatorial *= controle
    controle -= 1
print('O fatorial de {} é {}'.format(numero, fatorial))
