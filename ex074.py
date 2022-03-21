from random import randint

n1 = randint(0, 9)
n2 = randint(0, 9)
n3 = randint(0, 9)
n4 = randint(0, 9)
n5 = randint(0, 9)
lista = (n1, n2, n3, n4, n5)
print(f'Os valores sorteados foram: {lista}')
print(f'O maior número foi {sorted(lista)[-1]} e o menor foi {sorted(lista)[0]}')
