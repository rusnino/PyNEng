# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
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
    print(template.format(vlan, mac, intf))
