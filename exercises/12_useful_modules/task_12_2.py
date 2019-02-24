# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

import ipaddress
import subprocess

def check_ip_availability(ip_addresses_list):
    '''

    :param ip_addresses_list:
    :return: list_available, list_unavailable
    '''
    # print(ip_addresses_list)
    list_available = []
    list_unavailable =[]
    for ip_address in ip_addresses_list:
        if ping_ip(ip_address):
            list_available.append(ip_address)
        else:
            list_unavailable.append(ip_address)
    return list_available, list_unavailable


def convert_ip_range_to_list(ip_range):
    ip_list = []
    ip_range_list = ip_range.split('-')
    ip_len = int(ip_range_list[1].split('.')[-1]) - int(ip_range_list[0].split('.')[-1]) + 1
    for i in range(ip_len):
        ip_list.append(str(ipaddress.ip_address(ip_range.split('-')[0]) + i))

    return ip_list


def ping_ip(ip_address):
    '''
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    '''
    reply = subprocess.run(
        ['ping', '-c', '1', '-n', '-t', '1', ip_address],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')
    if reply.returncode == 0:bear
        return True
    else:
        return False

def extend_ip_address_list(ip_addresses_list):
    '''

    :param ip_addresses_list:
    :return: extended_ip_address_list
    '''
    extended_ip_address_list = []
    for string in ip_addresses_list:
        if len(string.split('-')) == 1:
            extended_ip_address_list.append(string)
        else:
            extended_ip_address_list.extend(convert_ip_range_to_list(string))
    return extended_ip_address_list

ip_addresses_list = ['192.168.0.5-192.168.0.6', '192.168.201.1', '8.8.8.8', '3.8.8.8', '10.1.1.1-10']
list_available, list_unavailable = check_ip_availability(extend_ip_address_list(ip_addresses_list))

print('Available: ', list_available)
print('Unavailable: ', list_unavailable)