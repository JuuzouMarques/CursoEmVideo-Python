lista = ()
for i in range(1, 5):
    nome = input(f'Insira o nome do seu {i}° produto: ')
    preco = float(input(f'Insira o preço do seu {i}° produto: R$ '))
    lista += (nome, preco)

print('{0}\n{1:^30}\n{0}'.format('-' * 30, 'PRODUTOS DISPONÍVEIS'))
for i in range(0, len(lista), 2):
    print('{:>10}:{}R$ {:.2f}'.format(lista[i], '-' * 10, lista[+ 1]))