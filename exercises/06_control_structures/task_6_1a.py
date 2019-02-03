# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

correct_address = True

ip_address = input('Enter IP-address: ')
ip_address_num_list = ip_address.split('.')
if len(ip_address_num_list) != 4:
    print("Incorrect IPv4 address" + " len check")
    correct_address = False
else:
    for i in range (len(ip_address_num_list)):
        try:
            if int(ip_address_num_list[i]) <0 or int(ip_address_num_list[i]) > 255:
                print("Incorrect IPv4 address" + " try " + str(i))
                correct_address = False
                break
        except ValueError:
            print("Incorrect IPv4 address" + " except " + str(i))
            correct_address = False
            break


#print(ip_address_num_list, correct_address)


if correct_address:
    for i in range (4):
    	ip_address_num_list[i] = int(ip_address_num_list[i])
    
    
    if ip_address_num_list[0] >=1 and ip_address_num_list[0] <=223:
    	print('unicast')
    elif ip_address_num_list[0] >=224 and ip_address_num_list[0] <=239:
    	print('multicast')
    elif ip_address_num_list[0] == 255 and ip_address_num_list[1] == 255 and ip_address_num_list[2] == 255 and ip_address_num_list[3] == 255:
    	print('local broadcast')
    elif ip_address_num_list[0] == 0 and ip_address_num_list[1] == 0 and ip_address_num_list[2] == 0 and ip_address_num_list[3] == 0:
    	print('unassigned')
    else:
        print('unused')