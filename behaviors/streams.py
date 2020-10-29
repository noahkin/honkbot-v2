import discord

class Streams:
    streamBank = [
        {'name': 'wolf', 'link': 'https://explore.org/livecams/currently-live/wolf-cam-1'},
        {'name': 'bear', 'link': 'https://explore.org/livecams/brown-bears/brown-bear-salmon-cam-brooks-falls'},
        {'name': 'jelly', 'link': 'https://explore.org/livecams/under-the-water/seajelly-cam'},
        {'name': 'lofi', 'link': 'https://www.youtube.com/watch?v=5qap5aO4i9A'}
    ]

    def get_stream(self, msgContent):
        streamObj = next((x for x in self.streamBank if x['name'] in msgContent), None)
        return streamObj['link']

    async def send_stream(self, message, msgContent):
        stream = self.get_stream(msgContent)
        if stream:
            await message.channel.send(stream) 
