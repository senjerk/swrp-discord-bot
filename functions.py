import os
import datetime
import a2s
import requests
from bs4 import BeautifulSoup


def format_date(date):
    months = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря'
    }
    minute = date.minute
    if date.minute == 0:
        minute = "00"
    return f"{date.hour}:{minute} {date.day} {months[date.month]} {date.year}"


def get_utc3_time():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).astimezone(
        datetime.timezone(datetime.timedelta(hours=3)))


def get_data() -> dict:
    headers = {
        "User-Agent": os.getenv("USER_AGENT"),
        "Accept": os.getenv("ACCEPT"),
        "Accept-Encoding": os.getenv("ACCEPT_ENCODING"),
        "Accept-Language": os.getenv("ACCEPT_LANGUAGE"),
        "Accept-Charset": os.getenv("ACCEPT_CHARSET"),
        "Cookie": os.getenv("COOKIE")
    }

    response = requests.get(os.getenv("URL"), headers=headers)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        location = soup.find("h1", id="location").text.strip()
        event = soup.find("h2", id="event").text.strip()

        data = {"location": location, "event": event}
        return data


def get_ip() -> tuple:
    ip = (os.getenv("SERVER_ADDRESS"), int(os.getenv("SERVER_PORT")))
    return ip


def get_players_count(ip: tuple) -> int:
    return len(a2s.players(ip))
