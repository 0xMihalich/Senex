from get_json import get_json


def lat_lon() -> tuple:
    dict_json = get_json(f'https://geolocation-db.com/json')
    return dict_json['latitude'], dict_json['longitude']
