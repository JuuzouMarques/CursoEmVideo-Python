estudantes = []
aluno = []
notas = []
while True:
    aluno.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    estudantes.append(aluno[:])
    aluno.clear()
    notas.clear()
    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N': break

print('-=' * 30)
print(f'{"N°":<3}{"NOME":<15}{"MÉDIA":>5}')
print('-' * 30)
for i, aluno in enumerate(estudantes):
    print(f'{(i):<3}{aluno[0]:<15}{((aluno[1][0] + aluno[1][1]) / 2):>5}')
print('-' * 30)

while True:
    resposta = int(input('Mostrar notas de qual aluno? (999 interrrompe): '))
    if resposta == 999:
        break
    print(f'Notas de {estudantes[resposta][0]} são {estudantes[resposta][1]}')
