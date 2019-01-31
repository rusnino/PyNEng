#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


#Reformat templates to string type
access_template = '\n'.join(access_template)
trunk_template = '\n'.join(trunk_template)

#Create dictionary to switch between templates
dct = {'access': access_template, 'trunk': trunk_template}
prompt_dict = {'access':'Enter VLAN number: ', 'trunk': 'Enter allowed VLANs: ' }

#Input variables
mode = input("Enter interface mode (access/trunk): ")
interface = input("Enter interface type and number: ")
vlans = input(prompt_dict['{}'.format(mode)])

print('interface {}\n'.format(interface) + dct['{}'.format(mode)].format(vlans))