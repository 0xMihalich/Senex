from dt import dt, timestamps
from sqlbase import conn
from unpack import unpack


def history_data(timezone: int) -> list:
    out = []
    with conn:
        cur = conn.cursor()
        for time in (0, 1):
            start, stop = timestamps(time, timezone)
            cur.execute(f'SELECT temp FROM weather WHERE dt >= {start} and  dt <= {stop};')
            temp = set(unpack(cur.fetchall()))
            cur.execute(f'SELECT weather FROM weather WHERE dt >= {start} and  dt <= {stop};')
            weather = unpack(cur.fetchall())
            out.append((min(temp), max(temp), max(weather)))
            if time == 1:
                out.append(dt(stop))
            del start, stop, temp, weather
    return out
