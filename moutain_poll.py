#coding=utf-8
responses = {}

#����һ����־ָ�������Ƿ����
polling_active = True

while polling_active:
	#��ʾ���뱻�����ߵ����ֺͻش�
	name = input('\nwhat is your name? ')
	response = input('which moutain would you like to climb someday? ')
	
	#���𰸴������ֵ���
	responses[name] = response
	
	#�����Ƿ�����Ҫ�������
	repeat = input('would you like to let another person respond?(y/n) ')
	if repeat == 'n':
		polling_active = False
		
	#���������ʾ���
	print('\n---polling results---')
	for name, response in responses.items():
		print(name + ' would like to climb '+ response +'.') 
