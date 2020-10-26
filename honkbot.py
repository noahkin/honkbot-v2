import discord
from discord.utils import get
import goose_cli
from auth import token
from datetime import datetime
import time
from behaviors.emoji import Emoji
from behaviors.bday import Bday
from behaviors.honk import Honk

emoji = Emoji()
bday = Bday()
honk = Honk()
class Client(discord.Client):
    # Runs when bot has finished initializing
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await goose_cli.run_cli(client) # Run any relevant CLI args passed to honkbot
    
    # Runs for each message in the server
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        ## Various bot commands below:
        if message.author != self.user: # Needs to check dev instance as well
            msg = message.content.lower()
            await emoji.send_emoji(msg)
            await bday.send_bday(msg)
            await honk.send_honk(msg)
# Launch bot
client = Client()
print(token)
client.run(token)
