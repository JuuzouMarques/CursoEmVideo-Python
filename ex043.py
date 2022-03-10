altura = float(input('Digite a sua altura em metros: '))
massa = float(input('Digite a sua massa em kg: '))
imc = massa / (altura ** 2)
print('Seu IMC: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Móbida')
