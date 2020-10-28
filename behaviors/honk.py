import discord
import time
import random
import important_files
import re

class Honk:
    honkish = re.compile(r'.*[h]+[o]+[n]+[k]+.*')
    honkBank = [
        'honk',
        'nice honkers',
        'you honked?',
        'Horn if yer Honky!!',
        'This goose is looooose',
        'U wanna have my eggs baby??',
        'wonderbread or gtfo bitch',
        'u down 4 this down?',
        'HONK HONK HONNNNKKKKKKKK OH FUCK HONK ME AHHHH HONKKKKKK',
        'hEIL hONkLER',
        'I\'m gonna hoooooooooooooonk',
        'V formation yall'
    ]

    def get_response(self, msgContent):
        if msgContent == 'hey honkbot':
            time.sleep(3) # delay before honk
            return 'hey'
        elif 'honk' in msgContent:
            return random.choice(self.honkBank)
        elif self.is_honky(msgContent):
            return self.is_honkbot_impressed(len(msgContent))
        else:
            return False

    def is_honky(self, msgContent):
        if self.honkish.match(msgContent):
            return True

    def is_honkbot_impressed(self, charCount):
        if charCount >= 10 and charCount <= 20:
            return 'WOW nice honk!'
        elif charCount >= 21 and charCount <= 30:
            return 'Well color me honked!'
        elif charCount >= 31 and charCount <= 40:
            return 'You sir, are master of the honks ;)'
        elif charCount >=41 and charCount <= 50:
            return 'oooo baby u gonna make me honk all over my featherssss'
        elif charCount >= 51 and charCount <= 60:
            return 'STOP IT RIGHT THERE! IM AFRAID YOUR UNDER ARREST FOR HONKIN WITHOUT A LICENSE!!!'
        elif charCount >= 61 and charCount <= 70:
            return 'o my god, honky, look at that honk. its sooo big, i cant believe its just so long and loud, i mean gross, look its just so I LIKE BIG HONKS AND I CANNOT LIE!!!'
        elif charCount >= 71 and charCount <= 80:
            return 'O honker who art in honkland, honkled be thy name. Your honkdom cum, your honk be done, in this pond as it is in honkland. Give us this day our daily wonderbread, and forgive us our repicys, as we have forgiven our repicitors. And lead us not into honktation, but deliver us...more bread'
        elif charCount >= 81 and charCount <= 90:
            return 'You are the one who honks'
        elif charCount >= 91 and charCount <= 100:
            return 'H O N K A D O N K I N M Y B A D O N K A D O N K ! ! !'
        elif charCount > 100:
            file = discord.File('C:/Users/jisana3/Desktop/New folder (2)/honkbot-v2/important_files/impressed_goose.jpg', filename='impressed_goose.jpg')
            return file
        else:
            return 'zzz'

    async def send_honk(self, message, msgContent):
        response = self.get_response(msgContent)
        if response:
            await message.channel.send(response)
