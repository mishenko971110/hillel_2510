'''
Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек - наприклад Timestamp 05:45:40, 
а в наступному повідомлені — Timestamp 05:45:09 (тут різниця heartbeat в 31 секунду)
Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один потік - Key TSTFEED0300|7E3E|0400
Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt
'''
from datetime import datetime
import logging


def filter_data(file_name, key):
    filtered_log = []

    with open(file_name, 'r') as f:
        content = f.read()
    conent_list = content.split('}')
    
    for line in conent_list:
        if key in line:
            index = line.find("Timestamp ")
            date_line = line[index + 10:index + 18]
            filtered_log.append(datetime.strptime(date_line, "%H:%M:%S"))
    
    return filtered_log


def create_logger(log_file_name):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger, file_handler


def requirements_analysis(filtered_log, log_file_name):
    logger = create_logger(log_file_name)

    for line_index in range(len(filtered_log) - 1):
        time_diff = (filtered_log[line_index] - filtered_log[line_index + 1]).total_seconds()

        if time_diff > 31 and time_diff < 33:
            logger.warning(f'Problem was from {filtered_log[line_index + 1].time()} to {filtered_log[line_index].time()}')
        elif time_diff >= 33:
            logger.error(f'Problem was from {filtered_log[line_index + 1].time()} to {filtered_log[line_index].time()}')
    
    logging.shutdown()


file_name = 'hblog.txt'
log_file_name = 'hb_test.log'

key = 'Key TSTFEED0300|7E3E|0400'

filtered_log = filter_data(file_name, key)
if filtered_log:
    requirements_analysis(filtered_log, log_file_name)
else:
    print("Жодних відповідних записів не знайдено.")
