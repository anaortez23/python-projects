
salary = int(input('Enter your salary: '))
yearOfEmp = int(input('Enter number of year: '))

if salary >= 30000:
    if yearOfEmp >= 2:
        print('You are qualified')
    else:
        print('You are not working long to be qualified')
else:
    print('Not qualified because you did not meet salary req.')
