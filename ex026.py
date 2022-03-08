frase = input('Digite uma frase: ').lower()
print('Na frase digitada, a letra \'a\' aparece {} vezes.'.format(frase.count('a')))
print('Primeiro na posição {}, e por último na posição {}.'.format(frase.find('a'), frase.rfind('a')))
