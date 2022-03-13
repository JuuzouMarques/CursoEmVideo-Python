sum = 0
for i in range(1, 7):
    num = int(input('{}° Valor: '.format(i)))
    if num % 2 == 0:
        sum += num
print('Soma dos valores pares digitados: {}'.format(sum))
