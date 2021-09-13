import discord
from behaviors.bday import Bday
from behaviors.honk import Honk
from behaviors.emoji import Emoji
from behaviors.help import Help
from behaviors.streams import Streams
from behaviors.scripture import Scripture
from behaviors.iHardlyKnowHer import IHardlyKnowHer
from neural.talkback import TalkBack

class MsgHandler:
    def __init__(self, message, gooseid, talkback):
        self.message = message
        self.msgContent = message.content.lower()
        self.gooseid = gooseid
        self.talkback = talkback

    async def delegate_behavior(self):
        if '^bday' in self.msgContent:
            bday = Bday()
            await bday.send_bday(self.message, self.msgContent)
        elif '^^' in self.msgContent:
            await self.talkback.respond(self.message, self.msgContent)
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
            img_class = self.gooseid.check_url(self.message.attachments[0].url).replace('_', ' ')
            if img_class == 'goose':
                await self.gooseid.goose_reaction(self.message, self.msgContent)
            else:
                await self.gooseid.other_reaction(self.message, self.msgContent, img_class)
        else:
            emoji = Emoji()
            honk = Honk()
            iHardlyKnowHer = IHardlyKnowHer()
            await emoji.send_emoji(self.message, self.msgContent)
            await honk.send_honk(self.message, self.msgContent)
            await iHardlyKnowHer.send(self.message, self.msgContent)
