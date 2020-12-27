import discord
from behaviors.bday import Bday
from behaviors.honk import Honk
from behaviors.emoji import Emoji
from behaviors.help import Help
from behaviors.streams import Streams
from behaviors.scripture import Scripture

class MsgHandler:
    def __init__(self, message, gooseid):
        self.message = message
        self.msgContent = message.content.lower()
        self.gooseid = gooseid

    async def delegate_behavior(self):
        if '^bday' in self.msgContent:
            bday = Bday()
            await bday.send_bday(self.message, self.msgContent)
        elif '^stream' in self.msgContent:
            streams = Streams()
            await streams.send_stream(self.message, self.msgContent)
        elif '^preach' in self.msgContent:
            scripture = Scripture()
            await scripture.send_verse(self.message, self.msgContent)
        elif '^help' in self.msgContent:
            help = Help()
            await help.send_help(self.message)
        elif self.message.attachments:
            # Check if there is a goose in the image:
            print(self.message.attachments[0].url)
            print(type(self.message.attachments[0].url))
            print(self.gooseid.check_for_goose(self.message.attachments[0].url))
            if self.gooseid.check_for_goose(self.message.attachments[0].url):
                await self.gooseid.goose_reaction(self.message, self.msgContent)
        else:
            emoji = Emoji()
            honk = Honk()
            await emoji.send_emoji(self.message, self.msgContent)
            await honk.send_honk(self.message, self.msgContent)
