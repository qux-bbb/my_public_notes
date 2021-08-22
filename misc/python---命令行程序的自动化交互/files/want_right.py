# coding:utf8
# python3

import random

first_num = str(random.randint(0, 10))
second_num = str(random.randint(0, 10))

first_input = input('input {}: '.format(first_num))
second_input = input('input {}: '.format(second_num))

if first_num==first_input and second_num==second_input:
    print('Right!')
else:
    print('Wrong!')
