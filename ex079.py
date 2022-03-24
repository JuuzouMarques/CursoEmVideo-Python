lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
print('-=' * 20)
lista.sort()
print(f'Você digitou os valores {lista}')
