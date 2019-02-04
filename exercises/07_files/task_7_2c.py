# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

config_cleared = []

with open(argv[1], 'r') as f:
    for line in f:
        ignore_flag = False
        for word in ignore:
            if word in line:
                ignore_flag = ignore_flag or True
        if not ignore_flag:
            config_cleared.append(line)

#print(config_cleared)
with open(argv[2], 'w') as f:
    f.writelines(config_cleared)