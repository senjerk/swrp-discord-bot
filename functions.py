import os

import a2s
import requests
from bs4 import BeautifulSoup


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
