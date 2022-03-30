matriz = []
linhas = []
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        linhas.append(n)
    matriz.append(linhas[:])
    linhas.clear()

print('-=' * 30)
for i in matriz:
    for j in i:
        print(f'[{j:^3}]', end='')
    print()
print('-=' * 30)

somaPares = somaColuna3 = somaLinha2 = 0
for i, linha in enumerate(matriz):
    for j, col in enumerate(linha):
        if col % 2 == 0: somaPares += col
        if j == 2: somaColuna3 += col
        if i == 1: somaLinha2 += col
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaColuna3}')
print(f'A soma dos valores da segunda linha é {somaLinha2}')
