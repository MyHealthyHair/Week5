#coding=utf-8
#���ȴ���һ������֤�û��б�
#��һ�����ڴ�������֤�û��Ŀ��б�
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

#��֤ÿ���û�ֱ��û��δ��֤�û�Ϊֹ
#��ÿ��������֤���б��Ƶ�����֤�û��б���
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print('verifying user: ' + current_user.title())
	confirmed_users.append(current_user)
	
#��ʾ��������֤���û�
print('\nthe following user have been confirmed: ')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
