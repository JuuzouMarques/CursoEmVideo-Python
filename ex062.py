primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = 0
while termo < 10:
    print('{} → '.format(primeiro + (termo * razao)), end='')
    termo += 1
resposta = 5
while resposta != 0:
    resposta = int(input('\nDeseja mostrar mais quantos termos? '))
    teste = 1
    while teste <= resposta:
        print('{} → '.format(primeiro + (termo * razao)), end='')
        termo += 1
        teste += 1
