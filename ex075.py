a = int(input('Digite algum valor: '))
b = int(input('Digite algum valor: '))
c = int(input('Digite algum valor: '))
d = int(input('Digite algum valor: '))
e = int(input('Digite algum valor: '))
tupla = (a, b, c, d, e)
print(f'O número 9 aparece {tupla.count(9)} vezes')
print(f'O número 3 foi digitado primeiro na posição {tupla.index(3) + 1}')
