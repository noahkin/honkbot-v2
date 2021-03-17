from aitextgen import aitextgen
import discord

class TalkBack:
    def __init__(self):
        self.ai = aitextgen('neural/static/gpt2_model_finetuned/pytorch_model.bin')

    async def respond(self, message, msgContent):
        response = self.ai.generate_one(prompt=msgContent[2:], max_length=40, temperature=1.1)
        await message.channel.send(response)