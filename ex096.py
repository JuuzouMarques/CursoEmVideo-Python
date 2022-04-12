def area(largura, comprimento):
    print(f'A área de um terreno de {largura:.2f}x{comprimento:.2f} é de {(largura * comprimento):.2f}m²')


# Programa Principal
print('Controle de terrenos')
print('--------------------')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
