APPID = 'ВАШ_API'
DATABASE = 'weather.db'

CITY = '''CREATE TABLE IF NOT EXISTS city (
          id INTEGER,
          name TEXT,
          state TEXT,
          yandex_id INTEGER,
          UNIQUE(id)
          );'''

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
