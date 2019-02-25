# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
from tabulate import tabulate

def ip_table(reachable_list, unreachable_list):
    '''

    :param reachable_list:
    :param unreachable_list:
    :return: 0
    '''

    table = [['Reachable', 'Unreachable']]
    if len(reachable_list) > len(unreachable_list):
        for i in range(len(reachable_list) - len(unreachable_list)):
            unreachable_list.append('')
    elif len(reachable_list) < len(unreachable_list):
        for i in range(len(unreachable_list) - len(reachable_list)):
            reachable_list.append('')

    for i in range(len(unreachable_list)):
            table.append([reachable_list[i], unreachable_list[i]])

    print(tabulate(table,
                   headers='firstrow',
                   # tablefmt="grid"
                   ))
    return 0


unreachable_list = ['192.168.0.5', '192.168.0.6', '3.8.8.8', '10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6', '10.1.1.7', '10.1.1.8', '10.1.1.9', '10.1.1.10']
reachable_list = ['1.1.1.1', '8.8.8.8', '1.1.1.1', '8.8.8.8', '1.1.1.1', '8.8.8.8', '1.1.1.1', '8.8.8.8', '1.1.1.1', '8.8.8.8', '1.1.1.1', '8.8.8.8', '1.1.1.1', '8.8.8.8']

ip_table(reachable_list, unreachable_list)