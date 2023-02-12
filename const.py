APPID = 'ВАШ_ТОКЕН_openweathermap'
IPAPI = 'ВАШ_ТОКЕН_ipinfo'
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
