from typing import NamedTuple


class weather(NamedTuple):
    dt: int
    temp: int
    feels: int
    pressure: int
    humidity: int
    weather: int
    icon: str
    wind: float
    degree: int


class city(NamedTuple):
    id: int
    lat: float
    lon: float
    sunrise: int
    sunset: int
    timezone: int


def weather_info(w_info: dict) -> weather:
    dt = w_info['dt']
    temp = round(w_info['main']['temp'])
    feels = round(w_info['main']['feels_like'])
    pressure = round(w_info['main']['grnd_level'] * 0.75006157584566)
    humidity = w_info['main']['humidity']
    weather_id = w_info['weather'][0]['id']
    icon = w_info['weather'][0]['icon']
    wind = round(w_info['wind']['speed'], 1)
    degree = w_info['wind']['deg']
    return weather(dt, temp, feels, pressure, humidity, weather_id, icon, wind, degree)


def city_info(w_info: dict) -> city:
    city_id = w_info['id']
    lat = w_info['coord']['lat']
    lon = w_info['coord']['lon']
    sunrise = w_info['sys']['sunrise']
    sunset = w_info['sys']['sunset']
    timezone = w_info['timezone']
    return city(city_id, lat, lon, sunrise, sunset, timezone)
