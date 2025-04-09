# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і 
# повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
from pathlib import Path

def get_xml_file_list(parent_dir):
    extension = '.xml'
    file_list = []
    files_with_extension = [f for f in parent_dir.iterdir() if f.suffix == extension]
    for file in files_with_extension:
        file_list.append(file)
    return file_list


def get_group_data_dict(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    group_data_dict = {}
    group_id = ''
    for child in root:
        for subchild in child:
            if subchild.tag == 'number':
                group_id = subchild.text
            if subchild.tag == 'timingExbytes':
                group_data_dict[group_id] = [subtag.text for subtag in subchild if subtag.tag == 'incoming'][0]
    return group_data_dict


def find_by_group(group_id, group_data_dict):
    return group_data_dict[group_id]

def check_entered_id(group_id, group_data_dict):
    if group_id in group_data_dict.keys():
        return True
    return 0

if __name__ == "__main__":
    parent_dir = Path('./lesson_13/ideas_for_test/work_with_xml')
    file_list = get_xml_file_list(parent_dir)

    group_id = input('Enter group_id: ')

    for file in file_list:
        if 'groups.xml' in str(file):
            group_data_dict = get_group_data_dict(file)
            try:
                if check_entered_id(group_id, group_data_dict):
                    incoming_value = find_by_group(group_id, group_data_dict)
                    print(f'Для group_id = {group_id} значення incoming = {incoming_value}')
                else:
                    print(f"Такого group_id з incoming у файлі не знайдено")
            except ET.ParseError as e:
                print(f"Помилка парсингу XML у файлі {file}")
            except FileNotFoundError:
                print(f"Файл не знайдено: {file}")
            except Exception as e:
                print(f"Невідома помилка у файлі {file}")
