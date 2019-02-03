#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_address = input('Enter IP-address: ')
ip_address_num_list = ip_address.split('.')
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