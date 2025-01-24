
import json
import csv
import yaml
from typing import Any, List, Dict, Union

def read_json(file_path: str, encoding: str = "utf-8") -> Union[Dict, List]:
    """Чтение данных из JSON файла"""
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)

def write_json(data: Union[Dict, List], file_path: str, encoding: str = "utf-8") -> None:
    """Запись данных в JSON файл"""
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def append_json(data: List[Dict], file_path: str, encoding: str = "utf-8") -> None:
    """Добавление данных в существующий JSON файл"""
    try:
        existing_data = read_json(file_path, encoding)
    except FileNotFoundError:
        existing_data = []
    
    if isinstance(existing_data, list):
        existing_data.extend(data)
    else:
        existing_data = [existing_data] + data
    
    write_json(existing_data, file_path, encoding)

def read_csv(file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> List[Dict]:
    """Чтение данных из CSV файла"""
    with open(file_path, 'r', encoding=encoding) as file:
        return list(csv.DictReader(file, delimiter=delimiter))

def write_csv(data: List[Dict], file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> None:
    """Запись данных в CSV файл"""
    if not data:
        return
    
    fieldnames = data[0].keys()
    with open(file_path, 'w', encoding=encoding, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)

def append_csv(data: List[Dict], file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> None:
    """Добавление данных в существующий CSV файл"""
    try:
        existing_data = read_csv(file_path, delimiter, encoding)
    except FileNotFoundError:
        existing_data = []
    
    existing_data.extend(data)
    write_csv(existing_data, file_path, delimiter, encoding)

def read_txt(file_path: str, encoding: str = "utf-8") -> str:
    """Чтение данных из текстового файла"""
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

def write_txt(data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Запись данных в текстовый файл"""
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(str(data))

def append_txt(data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Добавление данных в конец текстового файла"""
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(str(data))

def read_yaml(file_path: str) -> Union[Dict, List]:
    """Чтение данных из YAML файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

