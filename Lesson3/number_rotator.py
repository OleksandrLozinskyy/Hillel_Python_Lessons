first_int = int(input('Please, enter first integer, first_int =: '))
second_int = int(input('Please, enter second integer, second_int =: '))

print('You are entered first_int = {0}, second_int = {1}'.format(first_int, second_int))
print('Start rotating .....')
first_int = first_int + second_int
print('first_int = first_int + second_int =', first_int)
second_int = second_int - first_int
print('second_int = second_int - first_int =', second_int)
first_int = first_int + second_int
print('first_int = first_int + second_int =', first_int)
second_int = -second_int
print('second_int = -second_int = ', second_int)
print('The result of rotation is first_int = {0}, second_int = {1}'.format(first_int, second_int))


