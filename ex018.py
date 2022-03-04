from math import radians, sin, cos

angulo = float(input('Digite um angulo: '))
sin = sin(radians(angulo))
cos = cos(radians(angulo))
print('O seno do angulo {}° vale: {:.2f}, e seu cosseno vale: {:.2f}'.format(angulo, sin, cos))
