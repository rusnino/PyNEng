# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def generate_config_dict(filename):
    '''
    '''
    config_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith('!') and not check_ignore(line, ignore) and not line.startswith(' '):
                keyword = line.rstrip()
                config_dict[keyword] = []
            elif not line.startswith('!') and not check_ignore(line, ignore):
                config_dict[keyword].append(line.rstrip())
    final_dict={}
    for key_main, val in config_dict.items():
        if not any(string.startswith(2*' ') for string in val):
            final_dict[key_main]=[string.strip() for string in val]
        else:
            final_dict[key_main]={}
            for line in val:
                if line.startswith(2*' '):
                    final_dict[key_main][key_main_sub].append(line.lstrip())
                elif line.startswith(1*' '):
                    key_main_sub=line.lstrip()
                    final_dict[key_main][key_main_sub]=[]
    return(final_dict)
config_dict = generate_config_dict('config_r1.txt')

