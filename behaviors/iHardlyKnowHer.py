class IHardlyKnowHer:
    global exclusions = [
        "together",
        "whatever",
        "forever",
        "ever",
        "never",
        "her",
        "er",
        "cancer",
        "over",
        "other",
        "after",
        "later",
        "rather",
        "sister",
        "brother",
        "father",
        "mother",
        "whether",
        "either"
        ]

    def build_response(self, word):
        word = word.captialize()
        return f"{word}? I hardly know her!"
    
    async def send(self, message, msgContent):
        words = set(msgContent.split())
        for word in words:
            if word.lower()[-2] == 'er' and word not in exclusions:
                response = self.build_response(word)
                await message.channel.send(response)