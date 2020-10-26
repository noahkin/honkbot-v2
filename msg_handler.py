import discord
from behaviors.bday import Bday
from behaviors.honk import Honk
from behaviors.emoji import Emoji
from behaviors.help import Help

class MsgHandler:
    def __init__(self, message):
        self.message = message
        self.msgContent = message.content.toLower()

    async def delegate_behavior(self):
        if '!bday' in self.msgContent:
            bday = Bday()
            await bday.send_bday(self.message, self.msgContent)
        elif '!help' in self.msgContent:
            help = Help(self.message)
            await help.send_help(self.message)
        else:
            emoji = Emoji()
            honk = Honk()
            await emoji.send_emoji(self.message, self.msgContent)
            await honk.send_honk(self.message, self.msgContent)
            
        