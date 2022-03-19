while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if valor < 0:
        break
    for i in range(1, 11):
        print(f'{valor} X {i:2d} = {valor * i}')
    print('-' * 20)
print('Programa TABUADA encerrado! Volte Sempre!')
