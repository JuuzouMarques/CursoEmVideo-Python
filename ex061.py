primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = 0
while termo < 10:
    print('{} → '.format(primeiro + (termo * razao)), end='')
    termo += 1
