from random import randint

def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        n = randint(1, 10)
        print(n, end=' ')
        lst.append(n)
    print('PRONTO!')

def somaPar(lst):
    print(f'Somando os valores pares de {lst}, temos: ', end='')
    s = 0
    for n in lst:
        if n % 2 == 0: s += n
    print(s)
    

# Programa Principal
lista = []
sorteia(lista)
somaPar(lista)
