# EXAMPLE

from dotenv import load_dotenv  # import load_dotenv to load your .env file
from os import environ  # import environ
from disnake import Intents  # import intents
from disnake.ext.commands import Bot  # import Bot class

bot = Bot(
    command_prefix=".",  # your command prefix
    owner_ids=[298043305927639041],  # put your owner id in here
    intents=Intents.all(),  # so you can see users (required for blacklist)
)
bot.load_extension("disnake_debug")  # load debug extension. one command and that is debug


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")


if __name__ == "__main__":
    load_dotenv()
    bot.run(environ["TOKEN"])
