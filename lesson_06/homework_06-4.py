# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

import random

rand_list = [random.randint(0, 100) for _ in range(10)]
print('Random list: ', rand_list)

sum_even = sum(i for i in rand_list if i % 2 == 0)
print(f'Sum of even numbers is {sum_even}')
