import locale
from datetime import datetime, timedelta
from time import mktime
from typing import Tuple


def dt(timestamp: int=None) -> str:
    '''вывод даты в формате [день недели], [дата]'''
    
    locale.setlocale(locale.LC_ALL, "ru")
    strftime = "%A, %d.%m.%Y"
    if not timestamp:
        strftime += ", %H:%M"
        timestamp = datetime.now()
    else:
        timestamp = datetime.fromtimestamp(timestamp)
    return timestamp.strftime(strftime)


def timestamps(days: int=1) -> Tuple[int, int]:
    '''генерация двух timestamp с заданной датой с 00.00 до 21.00'''
    
    data = datetime.now() + timedelta(days=days)
    return tuple(int(mktime(datetime(data.year, data.month, data.day, t, 0, 0, 0).timetuple())) for t in (0, 21))
