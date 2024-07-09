from collections import Counter
from pprint import pprint

import re
import sys


def parse_log_line(line: str) -> dict:
    '''
    The function parses the string with log information,
    and transforms it to dictionary.
    '''
    pattern = (r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<date>\d{2}) '+
               r'(?P<time>\d{2}:\d{2}:\d{2}) (?P<log>[A-Z]+) ' +
               r'(?P<message>.+)')
    match_obj = re.match(pattern, line)
    if match_obj:
        return match_obj.groupdict()
        

def load_logs(file_path: str) -> list:
    '''
    The function reads a file and makes a list from it's strings.
    '''
    log_list = []
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            for line in file:
                log_list.append(line)
    except FileNotFoundError:
        print('The file has not been found! Give a correct path, please.')
    except PermissionError:
        print('You have no rights to work with the file!')
    except UnicodeDecodeError:
        print('The file can not be readed.')
    return log_list

def filter_logs_by_level(logs: list, level: str) -> list:
    '''
    The function filters a list by level.
    '''
    filtered_list = []
    for item in logs:
        if level.lower() in item.lower():
            filtered_list.append(item)
    return filtered_list

def count_logs_by_level(logs: list) -> dict:
    '''
    The function counts the numnber of logs from a list.
    '''
    logs_list = []
    for log_line in logs:
        if log_line:
            parsed_line = parse_log_line(log_line)
            if parsed_line:
                logs_list.append(parsed_line['log'])
    return Counter(logs_list)

def display_log_counts(counts: dict) -> None:
    '''
    The function paints a table from a dict.
    '''
    print('{:^10}|{:^10}'.format('Log level', 'Quantity'))
    print('-'*10 + '|' + '-'*10)
    for kay, val in counts.items():
        # print('{:<10}|{:^10}'.format(kay, val))
        print(f'{kay:<10}|{val:^10}')

if __name__ == '__main__':

    if len(sys.argv) > 1:
        log_file = sys.argv[1]
        display_log_counts(count_logs_by_level(load_logs(log_file)))
        if len(sys.argv) > 2:        
            log_level = sys.argv[2]
            pprint(filter_logs_by_level(load_logs(log_file), 
                                        log_level))
