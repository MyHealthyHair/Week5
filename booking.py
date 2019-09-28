message = input('how many tables you want to book?')
message = int(message)

if message > 8 :
	print('\nsorry, we have no table.')
else:
	print('we have your table.')
