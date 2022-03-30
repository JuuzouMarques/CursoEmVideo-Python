grupoPessoas = []
pessoa = []
maiorPeso = menorPeso = 0
while True:
    pessoa.append(input('Nome da pessoa: '))
    pessoa.append(float(input('Peso da pessoa: ')))
    grupoPessoas.append(pessoa[:])
    if maiorPeso == 0:
        maiorPeso = menorPeso = pessoa[1]
    else:
        if pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]
        elif pessoa[1] < menorPeso:
            menorPeso = pessoa[1]
    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    pessoa.clear()
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(grupoPessoas)} pessoas.')
print(f'O maior peso foi de {maiorPeso}kg. Peso de: ', end='')
for p in grupoPessoas:
    if p[1] == maiorPeso:
        print(p[0], end=', ')
print(f'\nO menor peso foi de {menorPeso}kg. Peso de: ', end='')
for p in grupoPessoas:
    if p[1] == menorPeso:
        print(p[0], end=', ')
