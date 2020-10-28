import discord

class Emoji:
    emojis = [{'name': 'repicy', 'code': 'a:repicy:644999601270685707', 'response': 'rEpIcY!'},
        {'name': 'cringe', 'code': 'kershrek:768886281773383762', 'response': 'cringe bro'},
        {'name': 'smh', 'code': 'smhmyhead:651848089224609793', 'response': 'my head'},
        {'name': 'nate', 'code': 'yetinate:520637149566205964', 'response': 'schweeeee'},
        {'name': 'fuck yeah', 'code': ':thicc:438569502637293568', 'response': 'hnnnnn'},
        {'name': 'billgiggity', 'code': ':billgiggity:585922690943025220', 'response': '#1 Power-Bottom in TX'},
        {'name': 'bill', 'code': ':bill:378712561832689674', 'response': 'kiss me in the rain'},
        {'name': 'michael', 'code': ':mike:768901680787488810', 'response': 'michael'},
        {'name': 'goose', 'code': ':goosechamp:551145779834781737', 'response': 'honk'},
        {'name': 'kyle', 'code': 'SexyKyle:388117155176120320', 'response': None},
        {'name': 'society', 'code': ':imdajokababy:563930572813107200', 'response': None},
        {'name': 'haha', 'code': ':haha:525009386867916830', 'response': None},
        {'name': 'zzz', 'code': ':kylesnooze:536758017169817612', 'response': None}]

    def get_emoji(self, msgContent):
        emojiData = next((x for x in self.emojis if x['name'] in msgContent), None)
        return emojiData

    async def send_emoji(self, message, msgContent):
        emoji = self.get_emoji(msgContent)
        if emoji:
            if emoji['response']:
                await message.channel.send(emoji['response'])
            if emoji['code']:
                await message.add_reaction(emoji['code'])
