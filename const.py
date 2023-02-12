APPID = '34556ca79c838ee4c06f6e3050d01e1b'
IPAPI = '74466aff7335cc'
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
