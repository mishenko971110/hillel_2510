'''
    Створіть масив зі строками, які будуть складатися з чисел, які розділені комою.
    Наприклад: ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,32"]
    Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
    Якщо є символи, що не є числами ("qwerty1,2,3" у прикладі), вам потрібно зловити вийняток і вивести "Не можу це зробити!"
    Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
    Для цього прикладу правильний вивід буде - 10, 60, "Не можу це зробити"
'''

from random import *

# generation of list string item
def list_item_generator(count_items):
    items = [str(randint(1, 50)) for _ in range(count_items)]
    if count_items > 0 and random() >= 0.5:
        items[0] += 'qwerty'
    return ','.join(items)

# generation list like example
def get_new_list(len_list, count_items):
    return [list_item_generator(count_items) for _ in range(len_list)]

# check list and calculate sum of items
def get_sum_of_list_items(new_list):
    result = []
    for item in new_list:
        try:
            sum_value = sum(int(x) for x in item.split(','))
            result.append(sum_value)
        except:
            result.append('Не можу це зробити!')
    return result


# example 
length_of_list = int(input('Enter the length of list: '))
count_items_in_list = int(input('Enter the item count of list: '))

new_list = get_new_list(length_of_list, count_items_in_list)

print('Generated list:\n', new_list)
print('Checked result:\n', get_sum_of_list_items(new_list))
