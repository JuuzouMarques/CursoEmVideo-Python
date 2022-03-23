tupla = (input('Digite algum valor: '),
        input('Digite algum valor: '),
        input('Digite algum valor: '),
        input('Digite algum valor: '),
        input('Digite algum valor: '))
print(f'O número 9 aparece {tupla.count(9)} vezes')
print(f'O número 3 foi digitado primeiro na posição {tupla.index(3) + 1}')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
