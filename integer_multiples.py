prompt = 'please enter a number, '
prompt +='and I will tell you if it is the integer multiples of 10. '

number = input(prompt)
number = int(number)

if number % 10 == 0:
	print('\nthe number ' + str(number) + ' is the integer multiples of 10.')
else:
	print('\nthe number ' + str(number) + ' is not.')
