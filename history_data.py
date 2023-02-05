import sqlite3

from dt import dt, timestamps
from const import DATABASE
from unpack import unpack


def history_data() -> list:
    out = []
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        for time in (0, 1):
            start, stop = timestamps(time)
            cur.execute(f'SELECT temp, feels FROM weather WHERE dt >= {start} and  dt <= {stop};')
            temp = set(unpack(cur.fetchall()))
            cur.execute(f'SELECT weather FROM weather WHERE dt >= {start} and  dt <= {stop};')
            weather = list(set(unpack(cur.fetchall())))
            weather.sort()
            out.append((min(temp), max(temp), *weather))
            if time == 1:
                out.append(dt(stop))
            del start, stop, temp, weather
    return out
