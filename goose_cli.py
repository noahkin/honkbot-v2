import sys
import discord

# Checks for any possible CLI args when first running
async def run_cli(client):
    # say
    # makes honkbot say stuff
    # usage: python honkbot.py channelname this is the message that will appear in channelname
    if len(sys.argv) > 2:
        if sys.argv[1] == 'say':
            message = ''
            for i in range(3, len(sys.argv)):
                message += sys.argv[i]
                message += ' '
            channel = discord.utils.get(client.get_all_channels(), guild__name='Gooseboys', name=sys.argv[2])
            await channel.send(message)