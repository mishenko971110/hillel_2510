# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і 
# повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
from pathlib import Path

def get_xml_file_list(parent_dir):
    extension = '.xml'
    file_list = []
    files_with_extension = [f for f in parent_dir.iterdir() if f.suffix == extension]
    # Виведення списку файлів з певним розширенням
    print(f"Список файлів з розширенням '{extension}':")
    for file in files_with_extension:
        file_list.append(file)
    return file_list


def find_by_group(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    # Читання та виведення даних з елементів XML-документу
    for child in root:
        print(child.tag, child.attrib)
        for subchild in child:
            print(subchild.tag, subchild.text)



parent_dir = Path('./lesson_13/ideas_for_test/work_with_xml')
file_list = get_xml_file_list(parent_dir)
for file in file_list:
    print(file)
    if 'groups.xml' in str(file):
        try:
            find_by_group(file)
        except ET.ParseError as e:
            print(f"Помилка парсингу XML у файлі {file}")
        except FileNotFoundError:
            print(f"Файл не знайдено: {file}")
        except Exception as e:
            print(f"Невідома помилка у файлі {file}")