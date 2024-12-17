# Завдання 1:

# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і 
# приберіть їх. Результат запишіть у файл result_<your_second_name>.csv


import csv


def open_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))
    return 0


def check_dublicates():
    return 0


def write_csv(data):
    with open('result_mishchenko.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

