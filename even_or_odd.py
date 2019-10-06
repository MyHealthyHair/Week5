number = input('enter a number, and I will tell you if it is even or odd: ')
number = int(number)

if number % 2 == 0:
	print('\nthe number ' + str(number) + ' is even.')
else:
	print('\nthe number ' + str(number) + ' is odd.')
