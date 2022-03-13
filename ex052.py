num = int(input('Digite um número inteiro: '))
for i in range(2, num):
    if num % i == 0:
        print('{} não é primo'.format(num))
        break
    if i == (num - 1):
        print('{} é primo'.format(num))
