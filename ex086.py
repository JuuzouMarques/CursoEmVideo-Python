matriz = []
linhas = []
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        linhas.append(n)
    matriz.append(linhas[:])
    linhas.clear()

for i in matriz:
    for j in i:
        print(f'[{j:^3}]', end='')
    print()
