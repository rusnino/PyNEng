#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

#num = int(input('Enter the number: '))
#word = input('Enter the word: ')
#num = int('15')
#word = 'perl'
num = int(argv[1])
word  = argv[2]

num_list = [num_list.pop(-1) for i in range(len(num_list))]
word_list = [word_list.pop(-1) for i in range(len(word_list))]

num_index = len(num_list) - num_list.index(num) -1
word_index = len(word_list) - word_list.index(word) -1
print('Index of last entry of number {} is: '.format(num) + str(num_index))
print('Index of last entry of word {} is: '.format(word) + str(word_index))