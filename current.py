from PyQt5.QtCore import QThread, QTimer

from const import APPID, INFO, WTHR
from degree import degree
from dt import timestamp
from entryes import *
from get_json import get_json
from history_data import history_data
from lat_lon import lat_lon
from sqlbase import conn
from suntime import suntime
from weather_type import WeatherType
from yandex_info import yandex_info


def current(update: bool=False, geo: tuple=None, timezone: int=0):
    try:
        if geo:
            lat, lon = geo
        else:
            lat, lon = lat_lon(update)
        link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={APPID}'
        w_info = get_json(link)
        return weather_info(w_info), city_info(w_info)
    except:
        with conn:
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM weather WHERE dt >= {timestamp(timezone) - 10800} ORDER BY dt LIMIT 1;')
            _weather = weather(*cur.fetchone())
            cur.execute('SELECT * FROM info;')
            _info = city(*cur.fetchone())
        return _weather, _info


def hystory(lat: float, lon: float):
    link = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lat}&units=metric&appid={APPID}'
    h_info = get_json(link)
    return tuple(weather_info(weather) for weather in h_info['list'])
    

def weather_values(update: bool=False, geo: tuple=None, timezone: int=0):
    w_i, c_i = current(update, geo, timezone)
    with conn:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM city WHERE id = {c_i.id};')
        for_city = cur.fetchone()
    return w_i, c_i, for_city[1:3], for_city[3]


def update_city(info: city_info):
    with conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS info;')
        cur.execute(INFO)
        cur.execute('INSERT INTO info(id, lat, lon, sunrise, sunset, timezone) VALUES(?, ?, ?, ?, ?, ?);', info)
        conn.commit()


def update_weather():
    try:
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT lat, lon, timezone FROM info;')
            lat, lon, timezone = cur.fetchone()
            h_i = hystory(lat, lon)
            cur.execute('DROP TABLE IF EXISTS weather;')
            cur.execute(WTHR)
            for w in h_i:
                _weather = (w.dt - timezone, w.temp, w.feels, w.pressure, w.humidity, w.weather, w.icon, w.wind, w.degree)
                cur.execute('INSERT INTO weather VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);', _weather)
                del _weather
            conn.commit()
        del lat, lon, timezone, h_i
    except:
        pass
    


class Current(QThread):

    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.timer=QTimer()
        self.timer.timeout.connect(self.set_values)
        self.set_values(True)

    def run(self):
        self.timer.start(60000)
    
    def set_values(self, update=False):
        ui = self.mainwindow
        w_i, c_i, city, yandex = weather_values(update, ui.geo, ui.timezone)
        ui.timezone = c_i.timezone
        update_city(c_i)
        if update:
            update_weather()
        ui.city.setText(', '.join(c for c in city if c))
        ui.temp.setText(f'{w_i.temp}°')
        ui.seticon(f'icons/{w_i.icon}.png')
        ui.weather.setText(WeatherType(w_i.weather)._name)
        ui.feels.setText(f'ощущается как: {w_i.feels}°')
        ui.sunrise.setText(f'восход: {suntime(c_i.sunrise)}')
        ui.sunset.setText(f'заход: {suntime(c_i.sunset)}')
        ui.wind.setText(f'ветер: {w_i.wind} м/с, {degree(w_i.degree)}')
        ui.humidity.setText(f'влажность: {w_i.humidity}%')
        ui.pressure.setText(f'давление: {w_i.pressure} мм рт. ст.')
        ui.yandex.setText(f'ситуация на дорогах по версии Яндекс: {yandex_info(yandex)}')
        
        try:
            today, tomorrow, str_tomorrow = history_data(ui.timezone)
            ui.today.setText(f'сегодня: от {today[0]}° до {today[1]}°, {WeatherType(today[2])._name}')
            ui.tomorrow.setText(f'завтра: {str_tomorrow}, от {tomorrow[0]}° до {tomorrow[1]}°, {WeatherType(tomorrow[2])._name}')
        except ValueError:
            pass
    
    def new_values(self, geo=None):
        self.timer.stop()
        self.mainwindow.geo = geo
        self.set_values(True)
        self.timer.start(60000)


class History(QThread):

    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.timer=QTimer()
        self.timer.timeout.connect(self.history)

    def run(self):
        self.timer.start(10800000)
    
    def history(self):
        ui = self.mainwindow
        ui.current.timer.stop()
        ui.current.set_values(True)
        ui.current.timer.start(60000)
        
