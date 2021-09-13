class IHardlyKnowHer:
    def build_response(self, word):
        word = word.captialize()
        return f"{word}? I hardly know her!"

    async def send(self, message, msgContent):
        words = msgContent.split()
        for word in words:
            if word.lower()[-2] == 'er':
                response = self.build_response(word)
                await message.channel.send(response)