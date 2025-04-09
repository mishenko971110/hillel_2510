# Завдання 1:

# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і 
# приберіть їх. Результат запишіть у файл result_<your_second_name>.csv

import csv

def open_csv(file_name):
    data = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def check_duplicates(data1, data2):
    combined_data = data1 + data2
    unique_data = []
    seen = set()
    for row in combined_data:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(row)
    return unique_data


def write_csv(data):
    with open('result_mish.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print("Результат записано у файл 'result_mish.csv'")


if __name__ == "__main__":
    file_1 = './lesson_13/ideas_for_test/work_with_csv/random.csv'
    file_2 = './lesson_13/ideas_for_test/work_with_csv/random-michaels.csv'

    data1 = open_csv(file_1)
    data2 = open_csv(file_2)

    unique_data = check_duplicates(data1, data2)

    write_csv(unique_data)