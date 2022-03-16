n = int(input('Quantos números da sequência Fibonacci você deseja ver? '))

first = 0
sec = 1
print('{} → {} → '.format(first, sec), end='')
while n > 2:
    first, sec = sec, (first + sec)
    print('{} → '.format(sec), end='')
    n -= 1
