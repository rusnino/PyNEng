#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
list_strings_vlan1 = command1.split()[-1].split(',')
list_strings_vlan2 = command2.split()[-1].split(',')
list_int_vlan1 = [int(vlan) for vlan in list_strings_vlan1]
list_int_vlan2 = [int(vlan) for vlan in list_strings_vlan2]
print(list(set(list_int_vlan1) & set(list_int_vlan2)))
