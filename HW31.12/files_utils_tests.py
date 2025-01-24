
from files_utils import *

def test_json_operations():
    # Тестовые данные для JSON
    test_data = [
        {"name": "Иван", "age": 25},
        {"name": "Мария", "age": 30}
    ]
    
    # Тестирование JSON операций
    write_json(test_data, "test.json")
    loaded_data = read_json("test.json")
    append_json([{"name": "Петр", "age": 35}], "test.json")
    
    print("JSON тесты выполнены")

def test_csv_operations():
    # Тестовые данные для CSV
    test_data = [
        {"имя": "Иван", "возраст": "25"},
        {"имя": "Мария", "возраст": "30"}
    ]
    
    # Тестирование CSV операций
    write_csv(test_data, "test.csv")
    loaded_data = read_csv("test.csv")
    append_csv([{"имя": "Петр", "возраст": "35"}], "test.csv")
    
    print("CSV тесты выполнены")

def test_txt_operations():
    # Тестовые данные для TXT
    test_data = "Это тестовая строка\nВторая строка"
    
    # Тестирование TXT операций
    write_txt(test_data, "test.txt")
    loaded_data = read_txt("test.txt")
    append_txt("\nТретья строка", "test.txt")
    
    print("TXT тесты выполнены")

def test_yaml_operations():
    # Тестовые данные для YAML
    weather_app_config = """
    app_name: WeatherApp
    version: 1.0
    settings:
      api_key: your_api_key_here
      units: metric
      language: ru
    features:
      - current_weather
      - forecast
      - alerts
    """
    
    # Записываем конфигурацию в YAML файл
    with open("test.yaml", "w", encoding="utf-8") as f:
        f.write(weather_app_config)
    
    # Читаем и проверяем данные
    yaml_data = read_yaml("test.yaml")
    print("YAML тесты выполнены")
    print("Конфигурация погодного приложения:", yaml_data)

if __name__ == "__main__":
    test_json_operations()
    test_csv_operations()
    test_txt_operations()
    test_yaml_operations()
