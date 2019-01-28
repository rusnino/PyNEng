#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

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
mask_bin_string = '1' * int(mask) + '0' * (32-int(mask))
#print(mask_bin_string)

output_template = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''

print('Network:' + output_template.format(int(subnet.split('.')[0]), int(subnet.split('.')[1]), int(subnet.split('.')[2]), int(subnet.split('.')[3])))
print('Mask:' + '\n/' + mask + output_template.format(int(mask_bin_string[0:8],2), int(mask_bin_string[8:16],2), int(mask_bin_string[16:24],2), int(mask_bin_string[24:32],2)))