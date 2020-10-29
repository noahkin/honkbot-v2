import discord
from behaviors.streams import Streams

class Help:
    async def send_help(self, message):
        # Send Gooseboys secondary logo
        file = discord.File('important_files/GB_LOGO_SECONDARY.jpg', filename='GB_LOGO_SECONDARY.jpg')
        # Automatically populate with all available streams
        streams = Streams()
        stream_commands = ''
        for stream in streams.streamBank:
            stream_commands += ('\n^stream ' + stream['name'])

        # Generate message
        help_message = '''```
Thank u for choosing honkbot. Here is a list of words i understand:

^help
^bday, ^bday next''' + stream_commands + '''
^preach
        
Give me big honks.```'''

        await message.channel.send(file=file)
        await message.channel.send(help_message)
