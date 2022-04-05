numeros = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Pares: {numeros[0]}\nImpares: {numeros[1]}')
