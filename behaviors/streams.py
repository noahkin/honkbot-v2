import discord


class Streams:
    streamBank = [
        {'name': 'wolf', 'link': 'https://www.youtube.com/watch?v=SQfE_-sSdc4&feature=emb_logo'},
        {'name': 'bear', 'link': 'https://www.youtube.com/watch?v=IcWTPFnqOLo&feature=emb_logo'},
        {'name': 'jelly', 'link': 'https://www.youtube.com/watch?v=vUL-RX_aoOg&feature=emb_logo'},
        {'name': 'space', 'link': 'https://www.youtube.com/watch?v=DDU-rZs-Ic4&feature=emb_rel_err'},
        {'name': 'gorilla', 'link': 'https://www.youtube.com/watch?v=rgXWDk7rh4w&feature=emb_logo'},
        {'name': 'lofi', 'link': 'https://www.youtube.com/watch?v=5qap5aO4i9A'}
    ]

    def get_stream(self, msgContent):
        streamObj = next((x for x in self.streamBank if x['name'] in msgContent), None)
        return streamObj['link']

    async def send_stream(self, message, msgContent):
        stream = self.get_stream(msgContent)
        if stream:
            await message.channel.send(stream) 
