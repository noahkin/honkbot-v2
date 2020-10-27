import discord
import time
import random

class Honk:
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
    ]

    def get_response(self, msgContent):
        if msgContent == 'hey honkbot':
            time.sleep(3) # delay before honk
            return 'hey'
        elif 'honk' in msgContent:
            return random.choice(self.honkBank)
        else:
            return False

    async def send_honk(self, message, msgContent):
        response = self.get_response(msgContent)
        if response:
            await message.channel.send(response)
