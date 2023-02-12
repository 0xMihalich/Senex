from sqlbase import conn


def city_dict() -> dict:
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT name, state, lat, lon FROM city ORDER BY name;')
        result = {', '.join(i.lower() for i in (name, state) if i): (lat, lon) for (name, state, lat, lon) in cur.fetchall()}
    return result
