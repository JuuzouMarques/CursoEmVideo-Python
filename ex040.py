nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('APROVADO COM MÉDIA {:.1f}'.format(media))
elif media >= 5.0:
    print('EM RECUPERAÇÃO COM MÉDIA {:.1f}'.format(media))
else:
    print('REPROVADO COM MÉDIA {:.1f}'.format(media))
