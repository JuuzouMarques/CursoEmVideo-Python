def notas(*notas, conc=False):
    '''
    -> Função para analisar as notas e a situação de vários alunos
    :param notas: Várias notas a serem analisadas
    :param conc: Indica se o retorno deve conter o conceito da turma
    :return: Dicionário com a análise das notas
    '''
    retorno = dict()
    qtd = len(notas)
    maior = menor = media = 0
    for i, n in enumerate(notas):
        if i == 0:
            maior = menor = n
        else:
            if n > maior: maior = n
            if n < menor: menor = n
        media += n/len(notas)
    retorno['total'] = qtd
    retorno['maior'] = maior
    retorno['menor'] = menor
    retorno['media'] = media
    if conc:
        if media < 5:
            conceito = 'INSUFICIENTE'
        elif 5 <= media < 8:
            conceito = 'REGULAR'
        elif 8 <= media < 9:
            conceito = 'BOM'
        else:
            conceito = 'EXCELENTE'
        retorno['conceito'] = conceito
    return retorno


# Programa Principal
print(notas(5, 6, 7, 8, conc=True))
