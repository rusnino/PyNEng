#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
prefix = input('Enter IP prefix(eg. 10.1.1.0/24): ')
#print(prefix)

subnet, mask = prefix.split('/')
subnet_bin_string = '{:08b}{:08b}{:08b}{:08b}'.format(int(subnet.split('.')[0]),int(subnet.split('.')[1]),int(subnet.split('.')[2]),int(subnet.split('.')[3]))
subnet_bin_string = subnet_bin_string[:int(mask)] + (32-int(mask)) * '0'
subnet = [int(subnet_bin_string[0:8],2), int(subnet_bin_string[8:16],2), int(subnet_bin_string[16:24],2), int(subnet_bin_string[24:],2)]
#print(subnet)

mask_bin_string = '1' * int(mask) + '0' * (32-int(mask))
#print(mask_bin_string)

output_template = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''

print('Network:' + output_template.format(subnet[0], subnet[1], subnet[2], subnet[3]))
print('Mask:' + '\n/' + mask + output_template.format(int(mask_bin_string[0:8],2), int(mask_bin_string[8:16],2), int(mask_bin_string[16:24],2), int(mask_bin_string[24:32],2)))
