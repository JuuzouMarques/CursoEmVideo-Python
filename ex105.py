def notas(*notas, conc=False):
    '''
    -> Função para analisar as notas e a situação de vários alunos
    :param notas: Várias notas a serem analisadas
    :param conc: Indica se o retorno deve conter o conceito da turma
    :return: Dicionário com a análise das notas
    '''
    retorno = dict()
    retorno['total'] = len(notas)
    retorno['maior'] = max(notas)
    retorno['menor'] = min(notas)
    retorno['media'] = sum(notas)/len(notas)
    if conc:
        if retorno['media'] < 5:
            conceito = 'INSUFICIENTE'
        elif 5 <= retorno['media'] < 7:
            conceito = 'REGULAR'
        elif 7 <= retorno['media'] < 9:
            conceito = 'BOM'
        else:
            conceito = 'EXCELENTE'
        retorno['conceito'] = conceito
    return retorno


# Programa Principal
print(notas(5, 6, 7, 8, conc=True))
