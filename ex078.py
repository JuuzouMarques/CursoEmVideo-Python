lista = []
for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
print(f'Você digitou os valores {lista}')

teste = lista[:]
teste.sort()
print(f'O menor valor digitador foi {teste[0]} nas posições ', end='')
for c, n in enumerate(lista):
    if n == teste[0]: print(f'{c}... ', end='')   
print(f'\nO maior valor digitador foi {teste[-1]} nas posições ', end='')
for c, n in enumerate(lista):
    if n == teste[-1]: print(f'{c}... ', end='')
