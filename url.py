from urllib.request import Request, urlopen


def url(link: str) -> urlopen:
    return urlopen(Request(link))
