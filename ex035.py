lista = []
for i in range(3):
    lista.append(int(input('Digite o valor da reta {}: '.format(i + 1))))
lista.sort()

if lista[0] + lista[1] > lista[2]:
    print('As três retas podem formar um triangulo')
else:
    print('As três retas não podem formar um triangulo')
