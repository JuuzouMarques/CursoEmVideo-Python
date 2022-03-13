num = int(input('Digite um número: '))
print('Sua tabuada:')
for i in range(1, 11):
    print('{} x {:2} = {:2}'.format(num, i, num * i))
