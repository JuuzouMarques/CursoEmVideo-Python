lista = []
for i in range(3):
    lista.append(int(input('Digite o valor da reta {}: '.format(i + 1))))
lista.sort()

if lista[0] + lista[1] > lista[2]:
    if lista[0] == lista[2]:
        print('Forma um triângulo EQUILÁTERO')
    elif lista[0] == lista[1]:
        print('Forma um triângulo ISÓCELES')
    else:
        print('Forma um triângulo ESCALENO')
else:
    print('As três retas não podem formar um triângulo')
