import disnake
import a2s
from disnake.ext import commands, tasks
from functions import get_ip, get_data
from ui import create_embed, create_timeout_embed
import os
from timeout_decorator import timeout


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.events = False
        self.flag = True
        self.server_timeout = False

    @timeout(5)
    def my_function(self, ip: tuple) -> None:
        print(a2s.players(ip))

    @tasks.loop(seconds=10.0)
    async def bot_set_status(self) -> None:
        data = get_data()
        ip = get_ip()
        channel = self.bot.get_channel(int(os.getenv("CHANNEL_ID")))
        try:
            self.my_function(ip)
            if self.server_timeout:
                self.server_timeout = False
                await channel.send(embed=create_timeout_embed(data, False))
        except TimeoutError:
            if self.server_timeout is not True:
                self.server_timeout = True
                await channel.send(embed=create_timeout_embed(data, True))
                await self.bot.change_presence(
                    activity=disnake.Game(name="Сервер выключен."))
        if not self.server_timeout:
            if self.flag:
                if data["event"] != "База" and self.events is False:
                    self.events = True
                    embed = create_embed(data)
                    await channel.send(embed=embed)
                elif data["event"] == "База" and self.events is True:
                    self.events = False
                await self.bot.change_presence(activity=disnake.Game(name=f"{data['event']}, карта: {data['location']}"))
                self.flag = False
            else:
                await self.bot.change_presence(
                    activity=disnake.Game(name=f"Онлайн: {len(a2s.players(ip))}/{a2s.info(ip).max_players}"))
                self.flag = True

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot_set_status.start()


def setup(bot):
    bot.add_cog(Status(bot))
