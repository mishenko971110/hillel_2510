# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

import random

rand_list = [random.randint(0, 100) for _ in range(10)]
sum = 0

print('Random list: ', rand_list)

for i in rand_list:
    if i % 2 == 0:
        sum += i

print(f'Sum of even numbers is {sum}')
