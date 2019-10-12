#1
def make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print(toppings)
	
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#2
def make_pizza(*toppings):
	"""该书要制作的披萨"""
	print('\nmaking a pizza with the following toppings: ')
	for topping in toppings:
		print('- ' + topping)
	
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#3
def make_pizza(size, *toppings):
	"""该书要制作的披萨"""
	print('\nmaking a ' + str(size)+
	      '-inch pizza with the following toppings: ')
	for topping in toppings:
		print('- ' + topping)
	
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
