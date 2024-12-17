# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import json
import logging


logging.basicConfig(
    filename='json__mishchenko.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def check_json(file_name):
    with open(file_name, 'r') as file:
        json_string = json.load(file)
    
    try:
        data = json.loads(json_string)
        print(data)
    except json.JSONDecodeError as e:
        logging.error(f"Файл {file_name} не є валідним JSON: {e}")
