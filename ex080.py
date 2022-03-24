lista = []
for i in range(5):
    num = int(input('Digite um valor: '))
    c = 0
    add = False
    while c < len(lista):
        if num < lista[c]:
            lista.insert(c, num)
            print(f'Adicionado na posição {c} da lista')
            add = True
            break
        c += 1
    if not add:
        lista.append(num)
        print('Adicionado ao fim da lista.')
print('-' * 20)
print(f'Os valor digitados em ordem foram {lista}')
print('-' * 20)
