def maior(* num):
    print('Analisando os valores passados...')
    lista = list()
    for n in num:
        print(n, end=' ')
        lista.append(n)
    lista.sort()
    print(f'\nForam informados {len(num)} valores ao todo')
    print(f'Dos valores informados, o maior foi {lista[-1]}')

maior(5, 3, 9, 4, 6)
print('-' * 30)
maior(1, 2, 3)
