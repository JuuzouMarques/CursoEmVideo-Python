print('-' * 30)
print('BANCO DO BRASILEIRO')
print('-' * 30)
valor = int(input('Qual valor você quer sacar? R$ '))
valorRestante = valor

valores = [50, 20, 10, 1]
for i in valores:
    if valorRestante // i > 0:
        print(f'Total de {valorRestante // i} cédulas de R${str(i)}')
        valorRestante = valorRestante % i
