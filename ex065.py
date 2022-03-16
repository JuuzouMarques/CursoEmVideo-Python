sum = int(input('Digite um valor: '))
maior = sum
menor = sum
qtd = 1
continuar = input('Deseja continuar? (s/n)').lower()
while continuar == 's':
    num = int(input('Digite outro valor: '))
    sum += num
    qtd += 1
    if num > maior: maior = num
    if num < menor: menor = num
    continuar = input('Deseja continuar? (s/n)').lower()
avg = sum / qtd
print('Foram digitados {} números, e a média foi de {:.2f}'.format(qtd, avg))
print('O maior número lido foi {}, e o menor foi {}'.format(maior, menor))
