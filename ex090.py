aluno = dict()
aluno['Nome'] = input('Nome do aluno: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 8:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
