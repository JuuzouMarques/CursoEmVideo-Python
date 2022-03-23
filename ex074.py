from random import randint

lista = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os valores sorteados foram: {lista}')
# print(f'O maior número foi {sorted(lista)[-1]} e o menor foi {sorted(lista)[0]}')
print(f'O maior número foi {max(lista)} e o menor foi {min(lista)}')
