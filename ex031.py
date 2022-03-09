distancia = float(input('Digite a distância da viagem em quilometros: '))
if distancia <= 200:
    print('A viagem custará R${:.2f}'.format(distancia * 0.5))
else:
    print('A viagem custará R${:.2f}'.format(distancia * 0.45))
