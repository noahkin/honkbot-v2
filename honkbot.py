import discord
import goose_cli
from auth import token

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await goose_cli.run_cli(client)
    
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # honk
        if message.author != self.user:
            if 'honk' in message.content:
                await message.channel.send('honk')
            if 'kyle' in message.content:
                await message.channel.send('kyle')

client = Client()
client.run(token)
