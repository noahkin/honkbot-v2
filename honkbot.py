import discord
from discord.utils import get
import goose_cli
from auth import token
from datetime import datetime
import time
from msg_handler import MsgHandler
from neural.gooseid import GooseID

class Client(discord.Client):
    # Runs when bot has finished initializing
    async def on_ready(self):
        self.gooseid = GooseID()
        print('Logged on as {0}!'.format(self.user))
        await goose_cli.run_cli(client) # Run any relevant CLI args passed to honkbot
    
    # Runs for each message in the server
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author != self.user: # Needs to check dev instance as well
            msgHandler = MsgHandler(message, self.gooseid)
            await msgHandler.delegate_behavior() # manages all honk bot actions
            
# Launch bot
client = Client()
client.run(token)