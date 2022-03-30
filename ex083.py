expr = input('Digite a expressão: ')
par = 0
for simb in expr:
    if simb == '(':
        par += 1
    elif simb == ')':
        par -= 1
        if par == -1:
            break

if par == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
