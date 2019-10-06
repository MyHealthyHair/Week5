prompt = '\ntell me something , and I will repeat it back to you: '
prompt += "\nenter 'quit' to end the program."
message = ''
while message != 'quit':
	message = input(prompt)
if message != 'quit':
	print(message)
