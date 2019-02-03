# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
correct_address = False


while not correct_address:
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
        else:
            correct_address = True


#print(ip_address_num_list, correct_address)


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