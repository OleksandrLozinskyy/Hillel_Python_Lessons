year = int(input('Please enter year: '))

if year < 1900 or year > 1000000:
    print('Please try again. Enter year starts from 1900 to 1000000')
else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Entered year {0} is leap'.format(year))
            else:
                print('Entered year {0} is not leap'.format(year))
        else:
            print('Entered year {0} is leap'.format(year))
    else:
        print('Entered year {0} is not leap'.format(year))
