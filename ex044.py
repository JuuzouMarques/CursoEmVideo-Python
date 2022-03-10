precoProduto = float(input('Digite o preço do produto: R$ '))
print('''Digite a forma de pagamento:
[1] Dinheiro ou cheque
[2] Débito
[3] Crédito até 2X
[4] Crédito a partir de 3X''')
escolha = int(input('Sua escolha: '))

if escolha == 1:
    print('Você recebeu 10\% de desconto')
    print('PREÇO A PAGAR: R$ {:.2f}'.format(precoProduto * 0.9))
elif escolha == 2:
    print('Você recebeu 5\% de desconto')
    print('PREÇO A PAGAR: R$ {:.2f}'.format(precoProduto * 0.95))
elif escolha == 3:
    print('PREÇO A PAGAR: R$ {:.2f}'.format(precoProduto))
elif escolha == 4:
    print('Essa forma de pagamento gera 20\% de acréscimo')
    print('PREÇO A PAGAR: R$ {:.2f}'.format(precoProduto * 1.2))
else:
    print('OPÇÃO INVÁLIDA')
