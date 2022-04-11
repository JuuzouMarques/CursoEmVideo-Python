from datetime import date

trabalhador = dict()
trabalhador['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nascimento
trabalhador['ctps'] = int(input('Nº da Carteira de Trabalho (0 caso não haja): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['contratacao'] + 35
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
