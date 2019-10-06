prompt = '\nplease enter the name of a city you have visited:'
prompt += "\n(enter 'quit' when you are finished.)"

while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print('I wloud love to go to ' + city.title() +' !') 
