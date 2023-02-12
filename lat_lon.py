from const import IPAPI
from get_json import get_json
from sqlbase import conn


def lat_lon(update: bool=False) -> tuple:
    if update:
        dict_json = get_json(f'https://ipinfo.io/?token={IPAPI}')
        return (float(loc) for loc in dict_json['loc'].split(','))
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT lat, lon FROM info;')
        lat, lon = cur.fetchone()
        if not lat:
            return lat_lon(True)
    return lat, lon
