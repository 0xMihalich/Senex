from bs4 import BeautifulSoup

from url import url


def yandex_info(city: int) -> str:
    try:
        return BeautifulSoup(url(f'https://export.yandex.ru/bar/reginfo.xml?region={city}').read(), 'xml').find('hint').text.lower()
    except AttributeError:
        return 'нет информации'
    except Exception:
        return 'нет соединения'
