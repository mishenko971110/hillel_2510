# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import os
import json
import logging

logging.basicConfig(
    filename='json__mishe.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

folder_path = './lesson_13/ideas_for_test/work_with_json'


def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
    except (json.JSONDecodeError, FileNotFoundError, UnicodeDecodeError) as e:
        logging.error(f"Invalid JSON in file: {file_path} - {str(e)}")

if __name__ == "__main__":
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            validate_json(file_path)
