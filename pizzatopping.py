prompt = 'please enter the pizza topping you want: '
prompt += "\nenter 'quit' when you are finished. " 

while True:
	message = input(prompt)
	
	if message != 'quit':
		print('\nwe will add '+ message +' to the pizzas.')
	else:
		break
