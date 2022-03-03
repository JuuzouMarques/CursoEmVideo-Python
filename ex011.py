width = float(input('Digite a largura da parede em metros: '))
heigth = float(input('Digite a altura da parede em metros: '))
area = width * heigth
print('A área da parede vale {:.2f}m²'.format(area))
print('Como cada litro de tinta pinta 2m², será necessário {:.1f} litros'.format(area / 2))
