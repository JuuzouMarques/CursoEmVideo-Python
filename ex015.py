days = int(input('How many days rented? '))
kilometers = float(input('Haw many kilometers driven? '))
print('The total payable is: R${:.2f}'.format(days * 60 + kilometers * 0.15))
