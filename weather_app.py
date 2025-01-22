
import requests
from plyer import notification

# Константы
API_KEY = "23496c2a58b99648af590ee8a29c5348"
CITY = "Москва"

def get_weather(city: str, api_key: str) -> dict:
    """Получаем данные о погоде через API"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()

def format_weather_message(weather_dict: dict) -> str:
    """Форматируем данные в читаемое сообщение"""
    temp = weather_dict['main']['temp']
    feels_like = weather_dict['main']['feels_like']
    description = weather_dict['weather'][0]['description']
    
    return f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}"

def notify_weather(message: str) -> None:
    """Отправляем уведомление"""
    notification.notify(
        title=f'Погода в {CITY}',
        message=message,
        app_name='Weather App',
        app_icon=None
    )

def main():
    """Основная логика программы"""
    try:
        # Получаем данные о погоде
        weather_data = get_weather(CITY, API_KEY)
        # Форматируем сообщение
        weather_message = format_weather_message(weather_data)
        # Отправляем уведомление
        notify_weather(weather_message)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
