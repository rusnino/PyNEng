#!/usr/local/bin/python3

username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

password_check = False

while not password_check:
	if len(password) < 8:
		print('Пароль слишком короткий')
		input('Введите пароль еще раз: ')
	elif username in password:
		print('Пароль содержит имя пользователя')
		input('Введите пароль еще раз: ')
	else:
		print('Пароль для пользователя {} установлен!'.format(username))
		password_check = True