#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
print(ospf_route)
list_string_ospf = ospf_route.split()

output_string_template = '''
{0:<24}{6:<24}
{1:<24}{7:<24}
{2:<24}{8:<24}
{3:<24}{9:<24}
{4:<24}{10:<24}
{5:<24}{11:<24}
'''

print(output_string_template.format('Protocol:',
									'Prefix:', 
									'AD/Metric:', 
									'Next-Hop:', 
									'Last update:', 
									'Outbound Interface:', 
									list_string_ospf[0], 
									list_string_ospf[1], 
									list_string_ospf[2].strip('[]'), 
									list_string_ospf[4].strip(','), 
									list_string_ospf[5].strip(','), 
									list_string_ospf[6]
									)
)
