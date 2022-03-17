numero = int(input('Digite um número: '))
fatorial = numero
controle = numero - 1
while controle > 1:
    fatorial *= controle
    controle -= 1
print('O fatorial de {} é {}'.format(numero, fatorial))

# Resolução Curso em Vídeo
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{} x'.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)
