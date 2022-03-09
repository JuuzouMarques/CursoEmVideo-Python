salary = float(input('Enter a employee salary: '))
print('The new salary is ${:.2f}'.format(salary * 1.1 if salary > 1250.0 else salary * 1.15))
