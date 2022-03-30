pares = []
impares = []
numeros = [pares, impares]
for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
print('-=' * 30)
print(f'Pares: {pares}\nImpares: {impares}')
