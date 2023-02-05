from requests import Session


def get_json(link: str) -> dict:
    with Session() as session:
        with session.get(link) as resp:
            try:
                result = resp.json()
            except Exception:
                raise
    return result
