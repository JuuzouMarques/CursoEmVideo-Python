def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg).strip().replace(',', '.'))
        if entrada.isalpha() or entrada == '':
            break
        print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m')
    return float(entrada)
