times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
        'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
        'Ceará SC', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá',
        'Juventude', 'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')

print('=' * 20)
print(f'Lista de times do brasileirão: {times[:5]}')
print('=' * 20)
print(f'Os 5 primeiros são: {times[-4:]}')
print('=' * 20)
print(f'O 4 últimos são: {sorted(times)}')
print('=' * 20)
print('Corinthians está na {}ª posição'.format(times.index('Corinthians') + 1))
