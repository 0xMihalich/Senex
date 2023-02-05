import sqlite3
from time import time

from PyQt5.QtCore import QThread, QTimer

from const import APPID, DATABASE, INFO, WTHR
from entryes import *
from get_json import get_json
from lat_lon import lat_lon
from weather_type import WeatherType
from suntime import suntime
from degree import degree
from yandex_info import yandex_info
from history_data import history_data


def current():
    try:
        lat, lon = lat_lon()
        link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={APPID}'
        w_info = get_json(link)
        return weather_info(w_info), city_info(w_info)
    except:
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM weather WHERE dt >= {int(time()) - 10800} ORDER BY dt LIMIT 1;')
            _weather = weather(*cur.fetchone())
            cur.execute('SELECT * FROM info;')
            _info = city(*cur.fetchone())
        return _weather, _info


def hystory(lat: float, lon: float):
    link = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lat}&units=metric&appid={APPID}'
    h_info = get_json(link)
    return tuple(weather_info(weather) for weather in h_info['list'])
    

def weather_values():
    w_i, c_i = current()
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM city WHERE id = {c_i.id};')
        for_city = cur.fetchone()
    return w_i, c_i, for_city[1:3], for_city[3]


def update_city(info: city_info):
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS info;')
        cur.execute(INFO)
        cur.execute('INSERT INTO info(id, lat, lon, sunrise, sunset, timezone) VALUES(?, ?, ?, ?, ?, ?);', info)
        conn.commit()


class Current(QThread):

    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.timer=QTimer()
        self.timer.timeout.connect(self.set_values)
        self.set_values(True)

    def run(self):
        self.timer.start(60000)
    
    def set_values(self, history=False):
        ui = self.mainwindow
        w_i, c_i, city, yandex = weather_values()
        update_city(c_i)
        if history:
            ui.update_history()
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
        today, tomorrow, str_tomorrow = history_data()
        ui.today.setText(f'сегодня: от {today[0]}° до {today[1]}°, {", ".join(WeatherType(w)._name for w in today[2:])}')
        ui.tomorrow.setText(f'завтра: {str_tomorrow}, от {tomorrow[0]}° до {tomorrow[1]}°, {", ".join(WeatherType(w)._name for w in tomorrow[2:])}')
        


class History(QThread):

    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.timer=QTimer()
        self.timer.timeout.connect(self.history)
        self.history()

    def run(self):
        self.timer.start(10800000)
    
    def history(self):
        try:
            with sqlite3.connect(DATABASE) as conn:
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
