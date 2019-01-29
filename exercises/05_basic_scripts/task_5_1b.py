#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

prefix = argv[1]
#prefix = input('Enter IP prefix(eg. 10.1.1.0/24): ')

subnet, mask = prefix.split('/')

subnet_bin_string = '{:08b}{:08b}{:08b}{:08b}'.format(int(subnet.split('.')[0]),int(subnet.split('.')[1]),int(subnet.split('.')[2]),int(subnet.split('.')[3]))

subnet_bin_string = subnet_bin_string[:int(mask)] + (32-int(mask)) * '0'

subnet = [int(subnet_bin_string[0:8],2), int(subnet_bin_string[8:16],2), int(subnet_bin_string[16:24],2), int(subnet_bin_string[24:],2)]


mask_bin_string = '1' * int(mask) + '0' * (32-int(mask))

output_template = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''

print('Network:' + output_template.format(subnet[0], subnet[1], subnet[2], subnet[3]))
print('Mask:' + '\n/' + mask + output_template.format(int(mask_bin_string[0:8],2), int(mask_bin_string[8:16],2), int(mask_bin_string[16:24],2), int(mask_bin_string[24:32],2)))
