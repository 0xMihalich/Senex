from requests import Session
from bs4 import BeautifulSoup


def yandex_info(city: int) -> str:
    try:
        with Session() as session:
            with session.get(f"https://export.yandex.ru/bar/reginfo.xml?region={city}") as resp:
                content = resp.text
        return BeautifulSoup(content, 'xml').find('hint').text.lower()
    except AttributeError:
        return 'нет информации'
    except Exception:
        return 'нет соединения'
