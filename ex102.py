def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Fatorial a ser calculado
    :param show: (opicional) Mostra a conta
    :return: Fatorial de num.
    """
    print('-=' * 20)
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    if show:
        resp = f'{str(num)}! = '
        while num > 1:
            resp += f'{str(num)} x '
            num -= 1
        resp += f'{str(num)} = {str(fat)}'
        return resp
    else:
        return fat


# Programa Principal
print(fatorial(4))
print(fatorial(5, True))
print(fatorial(12, show=True))
