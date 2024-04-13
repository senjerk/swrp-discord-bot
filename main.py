import disnake
from disnake.ext import commands, tasks
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import a2s
import os

load_dotenv()
client = commands.Bot(command_prefix='/', intents=disnake.Intents.all())
client.flag = True


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


@tasks.loop(seconds=10.0)
async def bot_set_status() -> None:
    if client.flag:
        data = get_data()
        await client.change_presence(activity=disnake.Game(name=f"{data['event']}, карта: {data['location']}"))
        client.flag = False
    else:
        ip = get_ip()
        await client.change_presence(
            activity=disnake.Game(name=f"Онлайн: {len(a2s.players(ip))}/{a2s.info(ip).max_players}"))
        client.flag = True


@client.event
async def on_ready() -> None:
    bot_set_status.start()


if __name__ == '__main__':
    client.run(os.getenv("BOT_TOKEN"))
