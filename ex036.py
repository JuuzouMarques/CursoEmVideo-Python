valorCasa = float(input('Digite o valor da casa: RS'))
salario = float(input('Digite o salário: R$'))
tempo = int(input('Quantos anos pretende pagar: '))
prestacao = valorCasa / (tempo * 12)
if prestacao > salario * 0.3:
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO APROVADO')
print('{} prestações de R${:.2f}'.format(tempo * 12, prestacao))
