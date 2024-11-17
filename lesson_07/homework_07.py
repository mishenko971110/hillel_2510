# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_func(a, b):
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg_func(number_list):
    return sum(number_list)/len(number_list)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_line(line: str):
    return line[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def get_max_word(sentence_list: list):
    return max(sentence_list, key=lambda x:len(x))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# 6.4: Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
def sum_even_numbers(number_list):
    return sum(i for i in number_list if i % 2 == 0)


# task 8
# 5.1: Write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending. We should print up to five (5) first found elements

def get_filtered_price(car_data, search_criteria):
    year_criteria, engine_volume_criteria, price_criteria = search_criteria
    car_price_data = {}
    for car_name, car_info in car_data.items():
        if (car_info[1] >= year_criteria) and (car_info[2] >= engine_volume_criteria) and (car_info[4] <= price_criteria):
            car_price_data[car_name] = car_info[4]
    return car_price_data

def get_five_sorted_cars(car_price_data):
    sorted_car_price_list = [car for car in sorted(car_price_data.items(), key=lambda x:x[1])]
    return sorted_car_price_list[:5]


# task 9
# 3.7: Знайди остачу від діленя чисел
# Знайди остачу від діленя чисел:
# a) 8019 : 8
# b) 9907 : 9
def get_remainder_of_division(num1, num2):
    return num1 % num2

print(get_remainder_of_division(8019, 8))
print(get_remainder_of_division(9907, 9))


# task 10
# 4.10: Виведіть кількість слів останнього речення з sentences_list.
def count_words_in_last_sentence(sentences_list):
    words_list = sentences_list[len(sentences_list) - 1].split()
    return len(words_list)
