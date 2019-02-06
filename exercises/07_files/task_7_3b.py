# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
exact_vlan = input('Enter vlan number: ')
template = " {0:<7}{1:<17}{2:<}"
count = 0
table = []
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if count >= 6:
        	table.append(line.rstrip().split())
        count += 1
table.sort()
for vlan, mac, _, intf in table:
	if vlan == exact_vlan:
	    print(template.format(vlan, mac, intf))