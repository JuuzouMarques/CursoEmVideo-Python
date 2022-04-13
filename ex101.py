def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos. NÃO VOTA!'
    elif 18 <= idade < 60:
        return f'Com {idade} anos. VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos. VOTO OPICIONAL!'


# Programa Principal
print('-' * 40)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
