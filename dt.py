import locale
from datetime import datetime, timedelta
from time import mktime
from typing import Tuple


def dt(timestamp: int=None, timezone: int=0) -> str:
    '''вывод даты в формате [день недели], [дата]'''
    
    locale.setlocale(locale.LC_ALL, "ru")
    strftime = "%A, %d.%m.%Y"
    if not timestamp:
        strftime += ", %H:%M"
        timestamp = datetime.utcnow() + timedelta(seconds=timezone)
    else:
        timestamp = datetime.fromtimestamp(timestamp)
    return timestamp.strftime(strftime)


def timestamps(days: int=1, timezone: int=0) -> Tuple[int, int]:
    '''генерация двух timestamp с заданной датой с 00.00 до 21.00'''
    
    data = datetime.utcnow() + timedelta(days=days, seconds=timezone)
    return tuple(int(mktime(datetime(data.year, data.month, data.day, t, 0, 0, 0).timetuple())) for t in (0, 21))


def timestamp(timezone: int=0) -> int:
    ts = datetime.utcnow() + timedelta(seconds=timezone)
    return int(ts.timestamp())
