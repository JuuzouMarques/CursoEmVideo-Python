from time import sleep

def contador(inicio, fim, passo):
    if passo == 0 : passo = 1
    passo = abs(passo)
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio <= fim:
        fim += 1
    else:
        passo = -passo
        fim -= 1
    sleep(1)
    for i in range(inicio, fim, passo):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')


# Programa Principal
contador(0, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
