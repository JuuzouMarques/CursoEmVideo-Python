ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('{} é bissexto'.format(ano))
        else:
            print('{} não é bissexto'.format(ano))
    else:
        print('{} é bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
