# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess

def check_ip_addresses(ip_addresses_list):
    '''

    :param ip_addresses_list:
    :return: list_available, list_unavailable
    '''
    list_available = []
    list_unavailable =[]
    for ip_address in ip_addresses_list:
        if ping_ip(ip_address):
            list_available.append(ip_address)
        else:
            list_unavailable.append(ip_address)
    return list_available, list_unavailable

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
        ['ping', '-c', '3', '-n', '-t', '1', ip_address],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')
    if reply.returncode == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    ip_addresses_list = ['192.168.201.1', '8.8.8.8', '3.8.8.8']
    list_available, list_unavailable = check_ip_addresses(ip_addresses_list)

    print('Available: ', list_available)
    print('Unavailable: ', list_unavailable)


