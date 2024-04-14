from disnake.ext import commands, tasks
import disnake
import plotly.graph_objects as go
import os
import sqlite3
from datetime import datetime, timedelta
from functions import get_players_count, get_ip


class Statistics(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.conn = sqlite3.connect('statistics.db')
        self.connect = self.conn.cursor()
        self.connect.execute('''CREATE TABLE IF NOT EXISTS data
                             (timestamp TEXT, time INTEGER, players INTEGER)''')
        self.save_data.start()

    @tasks.loop(minutes=1)
    async def save_data(self):
        if datetime.now().minute % 5 == 0:
            self.connect.execute("INSERT INTO data (timestamp, time, players) VALUES (?, ?, ?)", (datetime.now().strftime("%d:%m:%y"), datetime.now().strftime("%H:%M"), get_players_count(get_ip())))
            self.conn.commit()

    @commands.slash_command(name="diagram", description="Показывает диаграмму онлайна.",
                            guild_ids=[int(os.getenv("GUILD_ID"))])
    async def diagram(self, interaction):
        seven_days_ago = datetime.now() - timedelta(days=7)
        seven_days_ago_str = seven_days_ago.strftime("%d:%m:%y")

        timestamp_query = f"'{seven_days_ago_str}'"

        rows = self.connect.execute(f"SELECT * FROM data WHERE timestamp >= {timestamp_query}").fetchall()

        hours = []
        players = []

        for row in rows:
            hours.append(row[0] + ' ' + row[1])
            players.append(row[2])

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hours, y=players, mode='lines+markers', name='Количество игроков'))
        fig.update_layout(title='Количество игроков на сервере за последние 7 дней',
                          xaxis_title='Время',
                          yaxis_title='Количество игроков')

        fig.write_image("players_count_chart.png")

        with open("players_count_chart.png", "rb") as file:
            image = disnake.File(file)
        await self.bot.get_channel(int(os.getenv("CHANNEL_ID"))).send(file=image)


def setup(bot):
    bot.add_cog(Statistics(bot))
