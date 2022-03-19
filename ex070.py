totalCompra = 0.0
produtosCaros = 0
precoMaisBarato = 0
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$ '))
    totalCompra += preco

    if preco > 1000.0:
        produtosCaros += 1
    if (precoMaisBarato == 0) or (preco < precoMaisBarato):
        precoMaisBarato = preco
        produtoMaisBarato = nome

    while True:
        escolha = input('Quer continuar? [S/N] ')[0].upper()
        if escolha in 'SN':
            break
    if escolha == 'N':
        break

print('----- FIM DO PROGRAMA -----')
print(f'O total da compra foi R$ {totalCompra:.2f}')
print(f'Temos {produtosCaros} produtos custando mais de R$ 1000.00')
print(f'E o produto mais barato foi {produtoMaisBarato} que custou R$ {precoMaisBarato:.2f}')
