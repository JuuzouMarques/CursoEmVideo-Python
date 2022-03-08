city = input('Enter a city name: ')
firstName = city.lower().split()[0]
print('{} starts with \'Santo\'? {}'.format(city, (firstName == 'santo')))
