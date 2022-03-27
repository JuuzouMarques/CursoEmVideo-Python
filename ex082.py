numeros = []
print('0 para parar')
while True:
  numero = int(input('Digite um valor: '))
  if numero == 0:
    break
  numeros.append(numero)
pares = []
impares = []
for n in numeros:
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)
