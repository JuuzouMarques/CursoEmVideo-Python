galera = list()
pessoa = dict()
mediaIdade = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa)
    mediaIdade += pessoa['idade']
    pessoa.clear()
    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
mediaIdade /= len(galera)

print('-=' * 30)
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'A média de idade do grupo é de {mediaIdade:.2f} anos')
print(f'Molieres cadastradas: ', end='')
for i in galera:
    if i['sexo'] == 'F':
        print(i['nome'], end=', ')
print('Lista de pessoas que estão acima da média de idade:')
for i in galera:
    if i['idade'] > mediaIdade:
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')

