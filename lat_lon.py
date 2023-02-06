from const import IPAPI
from get_json import get_json
from sqlbase import conn


def lat_lon(update: bool=False) -> tuple:
    if update:
        dict_json = get_json(f'https://api.ipgeolocation.io/ipgeo?apiKey={IPAPI}')
        return dict_json['latitude'], dict_json['longitude']
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT lat, lon FROM info;')
        lat, lon = cur.fetchone()
        if not lat:
            return lat_lon(True)
    return lat, lon
