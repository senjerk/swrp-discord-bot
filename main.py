from disnake.ext import commands
from dotenv import load_dotenv
import os

import disnake

cogs_list = []
load_dotenv()
client = commands.Bot(command_prefix='/', intents=disnake.Intents.all())


@client.slash_command(name='load', description='load cogs')
async def load(ctx: disnake.ApplicationCommandInteraction, extension):
    await ctx.send("> Wait for cog to load in.", ephemeral=True)
    try:
        client.load_extension(f"cogs.{extension}")
        await ctx.edit_original_message(f"> Cog `{extension}` are succesfully loaded.")
    except commands.ExtensionAlreadyLoaded:
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")
        await ctx.edit_original_message(f"> Cog `{extension}` are succesfully loaded.")


@load.autocomplete("extension")
async def autocomplete(self, string: str):
    string = string.lower()
    return [cog for cog in cogs_list if string in cog.lower()]


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        cogs_list.append(file[:-3])
        client.load_extension(f"cogs.{file[:-3]}")

if __name__ == '__main__':
    client.run(os.getenv("BOT_TOKEN"))