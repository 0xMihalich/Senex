APPID = 'ВАШ_API_https://openweathermap.org/'
IPAPI = 'ВАШ_API_https://app.ipgeolocation.io/'
DATABASE = 'weather.db'

INFO = '''CREATE TABLE IF NOT EXISTS info (
          id INTEGER,
          lat REAL,
          lon REAL,
          sunrise INTEGER,
          sunset INTEGER,
          timezone INTEGER
          );'''

WTHR = '''CREATE TABLE IF NOT EXISTS weather (
          dt INTEGER,
          temp INTEGER,
          feels INTEGER,
          pressure INTEGER,
          humidity INTEGER,
          weather INTEGER,
          icon TEXT,
          wind REAL,
          degree INTEGER
          );'''
