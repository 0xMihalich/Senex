from json import load

from url import url


def get_json(link: str) -> dict:
    return load(url(link))
