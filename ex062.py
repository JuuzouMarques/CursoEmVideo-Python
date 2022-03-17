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
print('FIM DO PRIMEIRO PROGRAMA\n\n')

# Resolução curso em vídeo
print('Gerador de PA\n{}'.format('-=' * 10))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM DO SEGUNDO PROGRAMA')
