lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N': break
print('-' * 30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na posição {lista.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista')
    