maiorIdade = 0
quantidadeHomens = 0
mulheresJovens = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    print('-' * 20)
    
    if idade > 18:
        maiorIdade += 1
    if sexo == 'M':
        quantidadeHomens += 1
    if sexo == 'F' and idade < 20:
        mulheresJovens += 1

    escolha = ''
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
print('===== FIM DO PORGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')
print(f'Ao todo temos {quantidadeHomens} homens cadastrados')
print(f'E temos {mulheresJovens} mulheres com menos de 20 anos')
