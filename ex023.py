number = int(input('Enter a number: '))

print('Unidade: {}'.format(number % 10))
print('Dezena: {}'.format(number // 10 % 10))
print('Centena: {}'.format(number // 100 % 10))
print('Milhar: {}'.format(number // 1000 % 10))
