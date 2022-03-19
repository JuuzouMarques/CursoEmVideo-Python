maiorIdade = 0
quantidadeHomens = 0
mulheresJovens = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo: [M/F] ')[0].upper()
        if sexo in 'MF':
            break
    print('-' * 20)
    
    if idade > 18:
        maiorIdade += 1
    if sexo == 'M':
        quantidadeHomens += 1
    if sexo == 'F' and idade < 20:
        mulheresJovens += 1

    while True:
        escolha = input('Quer continuar? [S/N] ')[0].upper()
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print('===== FIM DO PORGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')
print(f'Ao todo temos {quantidadeHomens} homens cadastrados')
print(f'E temos {mulheresJovens} mulheres com menos de 20 anos')
