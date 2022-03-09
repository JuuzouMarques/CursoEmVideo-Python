speed = int(input('Enter the speed car: '))

if speed > 80:
    multa = (speed - 80) * 7
    print('The fine to be paid is ${:.2f}'.format(multa))
