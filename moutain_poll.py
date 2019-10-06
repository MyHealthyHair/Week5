#coding=utf-8
responses = {}

#设置一个标志指出调查是否继续
polling_active = True

while polling_active:
	#提示输入被调查者的名字和回答
	name = input('\nwhat is your name? ')
	response = input('which moutain would you like to climb someday? ')
	
	#将答案储存在字典中
	responses[name] = response
	
	#看看是否还有人要参与调查
	repeat = input('would you like to let another person respond?(y/n) ')
	if repeat == 'n':
		polling_active = False
		
	#调查结束显示结果
	print('\n---polling results---')
	for name, response in responses.items():
		print(name + ' would like to climb '+ response +'.') 
