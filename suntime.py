from datetime import datetime


def suntime(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
